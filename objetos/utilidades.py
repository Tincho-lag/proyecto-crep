from objetos.usuario import Estudiante, Profesor
from collections import deque
from datetime import datetime

# utilidades para guardar y cargar materiales
def guardar_materiales(sistema, archivo="resources/data/materiales.txt"):
    """guarda todos los materiales del sistema en un archivo de texto."""
    try:
        with open(archivo, "w") as f:
            materiales = sistema.listar_materiales()
            for mat in materiales:
                # usar hasattr para diferenciar libro de recursos
                if hasattr(mat, 'get_isbn'):  # es un libro
                    linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_isbn()}|{mat.get_titulo()}|{mat.get_autor()}|{mat.get_ano_publicacion()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
                else:  # es un recurso generico
                    # los recursos genericos no tienen isbn, autor ni ano
                    linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
                f.write(linea)
    except Exception as e:
        print(f"error al guardar materiales: {e}")

def cargar_materiales(sistema, archivo="resources/data/materiales.txt"):
    """carga los materiales guardados desde un archivo de texto."""
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                # importamos aqui para evitar dependencia circular si no estan importadas en el main
                from objetos.elemento import Libro, Recursos
                
                if len(partes) == 8: 
                    libro = Libro(partes[0], partes[1], partes[2], partes[3], 
                                  partes[4], int(partes[5]), int(partes[6]), int(partes[7]))
                    sistema.agregar_material(libro)
                elif len(partes) == 4: 
                    recurso = Recursos(partes[0], partes[1], int(partes[2]), int(partes[3]))
                    sistema.agregar_material(recurso)
    except FileNotFoundError:
        print("archivo de materiales no encontrado. iniciando con catalogo vacio.")
    except Exception as e:
        print(f"error al cargar materiales: {e}")

# utilidades para guardar y cargar usuarios
def guardar_usuarios(sistema, archivo="resources/data/usuarios.txt"):
    with open(archivo, "w") as f:
        for usuario in sistema.usuarios.values():
            tipo = "estudiante" if isinstance(usuario, Estudiante) else "profesor"
            linea = f"{tipo}|{usuario.get_id()}|{usuario.get_nombre()}|{usuario.get_domicilio()}|{usuario.get_estado()}\n"
            f.write(linea)

def cargar_usuarios(sistema, archivo="resources/data/usuarios.txt"):
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 5:
                    tipo, id_usuario, nombre, domicilio, estado = partes
                    if tipo == "estudiante":
                        usuario = Estudiante(id_usuario, nombre, domicilio)
                    elif tipo == "profesor":
                        usuario = Profesor(id_usuario, nombre, domicilio)
                    else:
                        continue
                    if estado == "suspendido":
                        usuario.suspender(0)  # suspension indefinida (puedes ajustar esto)
                    sistema.agregar_usuario(usuario)
    except FileNotFoundError:
        print("archivo de usuarios no encontrado. iniciando con usuarios vacios.")

# utilidades para guardar y cargar prestamos
def guardar_prestamos(sistema, archivo="resources/data/prestamos.txt"):
    with open(archivo, "w") as f:
        for prestamo in sistema.prestamos:
            if prestamo.esta_activo():
                linea = f"{prestamo.get_id_prestamo()}|{prestamo.get_usuario().get_id()}|{prestamo.get_material().get_titulo()}|{prestamo.get_fecha_prestamo().isoformat()}|{prestamo.get_fecha_vencimiento().isoformat()}\n"
                f.write(linea)

def cargar_prestamos(sistema, archivo="resources/data/prestamos.txt"):
    try:
        from objetos.biblioteca import Prestamo  # importacion local para evitar circularidad
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 5:
                    id_prestamo, id_usuario, titulo_material, fecha_prestamo_str, fecha_venc_str = partes
                    usuario = sistema.usuarios.get(id_usuario)
                    material = sistema.buscar_material(titulo_material)
                    if usuario and material:
                        prestamo = Prestamo(id_prestamo, usuario, material, usuario.get_dias_prestamo())
                        prestamo._Prestamo__fecha_prestamo = datetime.fromisoformat(fecha_prestamo_str)  # acceso privado
                        prestamo._Prestamo__fecha_vencimiento = datetime.fromisoformat(fecha_venc_str)
                        sistema.prestamos.append(prestamo)
                        sistema.contador_prestamos = max(sistema.contador_prestamos, int(id_prestamo[1:]) + 1)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"error al cargar prestamos: {e}")

# utilidades para guardar y cargar reservas
def guardar_reservas(sistema, archivo="resources/data/reservas.txt"):
    with open(archivo, "w") as f:
        for titulo, cola in sistema.reservas.items():
            ids = ",".join(cola.toLista())
            f.write(f"{titulo}|{ids}\n")

def cargar_reservas(sistema, archivo="resources/data/reservas.txt"):
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 2:
                    titulo, ids_str = partes
                    ids = ids_str.split(",")
                    if titulo not in sistema.reservas:
                        sistema.reservas[titulo] = Cola()
                    for id_usuario in ids:
                        sistema.reservas[titulo].encolar(id_usuario)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"error al cargar reservas: {e}")

# utilidad para registrar historial
def registrar_historial(accion, usuario, material, archivo="resources/data/historial.txt"):
    with open(archivo, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | {accion} | {usuario.get_id()} | {material.get_titulo()}\n")

class Cola:
    # se implementa la cola para manejar la reserva
    def __init__(self):
        self.__items = deque()

    def estaVacia(self):
        # esto verifica si la lista esta vacia, si el valor es igual a 0 devuelve true(que significa que la cola esta vacia)
        return len(self.__items) == 0

    def encolar(self, item):
        # agrega un usuario al final de la cola
        self.__items.append(item)

    def desencolar(self):
        # elimina el primero que esta en la lista
        if self.estaVacia():
            raise IndexError("la cola esta vacia")
        return self.__items.popleft()

    def verFrente(self):
        # muestra el primero que esta en la lista
        if self.estaVacia():
            raise IndexError("la cola esta vacia")
        return self.__items[0]

    def verFinal(self):
        # muestra el ultimo de la lista
        if self.estaVacia():
            raise IndexError("la cola esta vacia")
        return self.__items[-1]

    def tamanio(self):
        # muestra el tamano de la lista
        return len(self.__items)

    def contiene(self, item):
        # recorre toda la lista hasta encontrar el usuario que le pediste
        return item in self.__items

    def limpiar(self):
        # vacia la lista completamente
        self.__items.clear()

    def invertir(self):
        # invierte la lista
        self.__items.reverse()

    def toLista(self):
        # muestra la lista en el orden que los agregaste
        return list(self.__items)

    def encolarFrente(self, item):
        # esto se usa para llevar a alguien al frente de la lista
        self.__items.appendleft(item)

    def __str__(self):
        # esto muestra todo el contenido de la lista
        return "cola: [" + ", ".join(map(str, self.__items)) + "]"