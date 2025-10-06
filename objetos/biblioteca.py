# objetos/biblioteca.py 
from  .nodo_arbol import ArbolBinario
class Prestamo:
    def __init__(self, id_prestamo, usuario, material, dias_prestamo):
        self.__id_prestamo = id_prestamo
        self.__usuario = usuario
        self.__material = material
        self.__dias_prestamo = dias_prestamo
        self.__activo = True

    def get_id_prestamo(self):
        return self.__id_prestamo
    
    def get_usuario(self):
        return self.__usuario 
    
    def get_material(self):
        return self.__material 
    
    def get_dias_prestamo(self):
        return self.__dias_prestamo
    
    def esta_activo(self):
        return self.__activo
    
    def finalizar(self):
        self.__activo = False


class SistemaBiblioteca:
    def __init__(self):
        self.arbol_materiales = None  # Importar ArbolBinario
        self.usuarios = {}  # id -> objeto Usuario
        self.prestamos = []
        self.reservas = {}  # isbn -> lista de ids de usuarios
        self.contador_prestamos = 1
    
    def agregar_material(self, material):
        if self.arbol_materiales is None:
                self.arbol_materiales = ArbolBinario()
        self.arbol_materiales.insertar(material)
    
    def buscar_material(self, titulo):
        if self.arbol_materiales is None:
            return None
        return self.arbol_materiales.buscar_por_titulo(titulo)
    
    def agregar_usuario(self, usuario):
        self.usuarios[usuario.get_id()] = usuario
    
    def realizar_prestamo(self, id_usuario, titulo_material):
        # Buscar usuario
        if id_usuario not in self.usuarios:
            return False, "Usuario no encontrado"
        
        usuario = self.usuarios[id_usuario]
        
        # Verificar si está activo
        if not usuario.estado_activo():
            return False, "Usuario suspendido"
        
        # Buscar material
        material = self.buscar_material(titulo_material)
        if material is None:
            return False, "Material no encontrado"
        
        # Verificar disponibilidad
        if not material.hay_disponibles():
            return False, "Material no disponible"
        
        # Verificar límite de préstamos
        if len(usuario.get_material_prestado()) >= usuario.get_limite_prestamos():
            return False, "Límite de préstamos alcanzado"
        
        # Realizar préstamo
        if material.prestar():
            prestamo = Prestamo(
                f"P{self.contador_prestamos:04d}",
                usuario,
                material,
                usuario.get_dias_prestamo()
            )
            self.prestamos.append(prestamo)
            usuario.prestar_material(material.get_isbn())
            self.contador_prestamos += 1
            return True, "Préstamo exitoso"
        
        return False, "Error al prestar"
    
    def realizar_devolucion(self, id_usuario, titulo_material):
        usuario = self.usuarios.get(id_usuario)
        if usuario is None:
            return False, "Usuario no encontrado"
        
        material = self.buscar_material(titulo_material)
        if material is None:
            return False, "Material no encontrado"
        
        # Buscar préstamo activo
        for prestamo in self.prestamos:
            if (prestamo.esta_activo() and 
                prestamo.get_usuario().get_id() == id_usuario and
                prestamo.get_material().get_titulo() == titulo_material):
                
                material.devolver()
                usuario.devolver_material(material.get_isbn())
                prestamo.finalizar()
                return True, "Devolución exitosa"
        
        return False, "Préstamo no encontrado"
    
    def crear_reserva(self, id_usuario, isbn):
        if isbn not in self.reservas:
            self.reservas[isbn] = []
        if id_usuario not in self.reservas[isbn]:
            self.reservas[isbn].append(id_usuario)
            return True
        return False
    
    def listar_materiales(self):
        if self.arbol_materiales is None:
            return []
        return self.arbol_materiales.listar_todos()

# persistencia de archivos (temporal revisar)


def guardar_materiales(sistema, archivo="resources/data/materiales.txt"):
    with open(archivo, "w") as f:
        materiales = sistema.listar_materiales()
        for mat in materiales:
            if hasattr(mat, 'get_isbn'):  # Es un Libro
                linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_isbn()}|{mat.get_titulo()}|{mat.get_autor()}|{mat.get_año_publicacion()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
            else:  # Es un Recurso genérico
                linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
            f.write(linea)

def cargar_materiales(sistema, archivo="resources/data/materiales.txt"):
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 8:  # Libro
                    from objetos.elemento import Libro
                    libro = Libro(partes[0], partes[1], partes[2], partes[3], 
                                  partes[4], int(partes[5]), int(partes[6]), int(partes[7]))
                    sistema.agregar_material(libro)
    except FileNotFoundError:
        pass



if __name__ == "__main__":
    from elemento import Libro
    from usuario import Estudiante, Profesor
    
    sistema = SistemaBiblioteca()
    
    # Crear materiales
    libro1 = Libro("REF001", "Libro", "978-123", "Cien años de soledad", "García Márquez", 1967, 2, 2)
    libro2 = Libro("REF002", "Libro", "978-456", "El Principito", "Saint-Exupéry", 1943, 1, 1)
    libro3 = Libro("REF003", "Libro", "978-789", "1984", "George Orwell", 1949, 3, 3)
    
    sistema.agregar_material(libro1)
    sistema.agregar_material(libro2)
    sistema.agregar_material(libro3)
    
    # Crear usuarios
    estudiante = Estudiante("EST001", "Ana García", "Tacuarembó 123")
    profesor = Profesor("PROF001", "Dr. Juan Pérez", "Rivera 456")
    
    sistema.agregar_usuario(estudiante)
    sistema.agregar_usuario(profesor)
    
    print("=== SISTEMA DE BIBLIOTECA ===")
    print(f"\nMateriales disponibles:")
    for mat in sistema.listar_materiales():
        print(f"  - {mat}")
    
    # Préstamo exitoso
    print(f"\n--- Préstamo 1 ---")
    exito, msg = sistema.realizar_prestamo("EST001", "El Principito")
    print(f"Resultado: {msg}")
    
    # Buscar material
    print(f"\n--- Búsqueda ---")
    encontrado = sistema.buscar_material("1984")
    print(f"Buscando '1984': {encontrado}")
    
    # Devolución
    print(f"\n--- Devolución ---")
    exito, msg = sistema.realizar_devolucion("EST001", "El Principito")
    print(f"Resultado: {msg}")
    
    # Guardar datos
    print(f"\n--- Guardando en archivo ---")
    guardar_materiales(sistema)
    print("Datos guardados en resources/data/materiales.txt")