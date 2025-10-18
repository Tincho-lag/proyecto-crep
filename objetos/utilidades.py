# objetos/utilidades.py
from objetos.usuario import Estudiante, Profesor
from collections import deque
from datetime import datetime

#  PERSISTENCIA DE MATERIALES 

def guardar_materiales(sistema, archivo="resources/data/materiales.txt"):
    """guarda todos los materiales del sistema en archivo txt"""
    try:
        with open(archivo, "w") as f:
            materiales = sistema.listar_materiales()
            for mat in materiales:
                # diferenciar entre libros y recursos genericos
                if hasattr(mat, 'get_isbn'):  # es un libro
                    linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_isbn()}|{mat.get_titulo()}|{mat.get_autor()}|{mat.get_ano_publicacion()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
                else:  # es un recurso generico (cargador, revista, etc)
                    linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
                f.write(linea)
    except Exception as e:
        print(f"error al guardar materiales: {e}")


def cargar_materiales(sistema, archivo="resources/data/materiales.txt"):
    # carga materiales desde archivo txt al iniciar el sistema
    try:
        with open(archivo, "r") as f:
            from objetos.elemento import Libro, Recursos
            
            for linea in f:
                partes = linea.strip().split("|")
                
                if len(partes) == 8:  # es un libro (8 campos)
                    libro = Libro(partes[0], partes[1], partes[2], partes[3], 
                                  partes[4], int(partes[5]), int(partes[6]), int(partes[7]))
                    sistema.agregar_material(libro)
                
                elif len(partes) == 4:  # es un recurso generico (4 campos)
                    recurso = Recursos(partes[0], partes[1], int(partes[2]), int(partes[3]))
                    sistema.agregar_material(recurso)
    
    except FileNotFoundError:
        print("archivo de materiales no encontrado. iniciando con catalogo vacio.")
    except Exception as e:
        print(f"error al cargar materiales: {e}")


#  PERSISTENCIA DE USUARIOS 

def guardar_usuarios(sistema, archivo="resources/data/usuarios.txt"):
    # guarda usuarios en archivo txt
    try:
        with open(archivo, "w") as f:
            for usuario in sistema.usuarios.values():
                # identificar tipo de usuario
                tipo = "estudiante" if isinstance(usuario, Estudiante) else "profesor"
                linea = f"{tipo}|{usuario.get_id()}|{usuario.get_nombre()}|{usuario.get_domicilio()}|{usuario.get_estado()}\n"
                f.write(linea)
    except Exception as e:
        print(f"error al guardar usuarios: {e}")


def cargar_usuarios(sistema, archivo="resources/data/usuarios.txt"):
    # carga usuarios desde archivo txt al iniciar el sistema 
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                
                if len(partes) == 5:
                    tipo, id_usuario, nombre, domicilio, estado = partes
                    
                    # crear usuario segun tipo
                    if tipo == "estudiante":
                        usuario = Estudiante(id_usuario, nombre, domicilio)
                    elif tipo == "profesor":
                        usuario = Profesor(id_usuario, nombre, domicilio)
                    else:
                        continue
                    
                    # restaurar estado de suspension si aplica
                    if estado == "suspendido":
                        usuario.suspender(0)  # suspension sin fecha (manual)
                    
                    sistema.agregar_usuario(usuario)
    
    except FileNotFoundError:
        print("archivo de usuarios no encontrado. iniciando sin usuarios.")
    except Exception as e:
        print(f"error al cargar usuarios: {e}")


#  PERSISTENCIA DE PRESTAMOS 

def guardar_prestamos(sistema, archivo="resources/data/prestamos.txt"):
    # guarda solo los prestamos activos en archivo txt
    try:
        with open(archivo, "w") as f:
            for prestamo in sistema.prestamos:
                if prestamo.esta_activo():
                    # guardar en formato iso para facil parseo
                    linea = f"{prestamo.get_id_prestamo()}|{prestamo.get_usuario().get_id()}|{prestamo.get_material().get_titulo()}|{prestamo.get_fecha_prestamo().isoformat()}|{prestamo.get_fecha_vencimiento().isoformat()}\n"
                    f.write(linea)
    except Exception as e:
        print(f"error al guardar prestamos: {e}")


def cargar_prestamos(sistema, archivo="resources/data/prestamos.txt"):
    # carga prestamos activos al iniciar el sistema
    try:
        from objetos.biblioteca import Prestamo
        
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                
                if len(partes) == 5:
                    id_prestamo, id_usuario, titulo_material, fecha_prestamo_str, fecha_venc_str = partes
                    
                    # buscar usuario y material
                    usuario = sistema.usuarios.get(id_usuario)
                    material = sistema.buscar_material(titulo_material)
                    
                    if usuario and material:
                        # recrear objeto prestamo
                        prestamo = Prestamo(id_prestamo, usuario, material, usuario.get_dias_prestamo())
                        
                        # restaurar fechas usando acceso a atributos privados
                        prestamo._Prestamo__fecha_prestamo = datetime.fromisoformat(fecha_prestamo_str)
                        prestamo._Prestamo__fecha_vencimiento = datetime.fromisoformat(fecha_venc_str)
                        
                        sistema.prestamos.append(prestamo)
                        
                        # actualizar contador para no repetir ids
                        num_prestamo = int(id_prestamo[1:])
                        sistema.contador_prestamos = max(sistema.contador_prestamos, num_prestamo + 1)
    
    except FileNotFoundError:
        pass  # no hay prestamos previos, normal en primera ejecucion
    except Exception as e:
        print(f"error al cargar prestamos: {e}")


# PERSISTENCIA DE RESERVAS (COLAS) 

def guardar_reservas(sistema, archivo="resources/data/reservas.txt"):
    # guarda las colas de espera por material
    try:
        with open(archivo, "w") as f:
            for titulo, cola in sistema.reservas.items():
                # convertir cola a lista de ids separados por comas
                ids = ",".join(cola.toLista())
                f.write(f"{titulo}|{ids}\n")
    except Exception as e:
        print(f"error al guardar reservas: {e}")


def cargar_reservas(sistema, archivo="resources/data/reservas.txt"):
    # carga las colas de espera al iniciar el sistema
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                
                if len(partes) == 2:
                    titulo, ids_str = partes
                    ids = ids_str.split(",")
                    
                    # recrear cola
                    if titulo not in sistema.reservas:
                        sistema.reservas[titulo] = Cola()
                    
                    for id_usuario in ids:
                        sistema.reservas[titulo].encolar(id_usuario)
    
    except FileNotFoundError:
        pass  # no hay reservas previas
    except Exception as e:
        print(f"error al cargar reservas: {e}")


# CLASE COLA (ESTRUCTURA FIFO) 

class Cola:
    # cola fifo para manejar reservas de materiales
    def __init__(self):
        # usar deque de collections (optimizado para colas)
        self.__items = deque()

    def estaVacia(self):
        # verifica si la cola esta vacia
        return len(self.__items) == 0

    def encolar(self, item):
        # agrega un elemento al final de la cola
        self.__items.append(item)

    def desencolar(self):
        # remueve y devuelve el primer elemento (fifo)
        if self.estaVacia():
            raise IndexError("la cola esta vacia")
        return self.__items.popleft()

    def verFrente(self):
        # muestra el primer elemento sin removerlo
        if self.estaVacia():
            raise IndexError("la cola esta vacia")
        return self.__items[0]

    def tamanio(self):
        # devuelve cantidad de elementos en la cola 
        return len(self.__items)

    def contiene(self, item):
        # verifica si un elemento esta en la cola
        return item in self.__items

    def toLista(self):
        # convierte la cola a lista para persistencia
        return list(self.__items)

    def __str__(self):
        # representacion en texto de la cola 
        return "cola: [" + ", ".join(map(str, self.__items)) + "]"

