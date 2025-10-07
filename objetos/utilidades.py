# objetos/utilidades.py
from objetos.usuario import Estudiante, Profesor

# utilidades para guardar y cargar materiales
def guardar_materiales(sistema, archivo="resources/data/materiales.txt"):
    """Guarda todos los materiales del sistema en un archivo de texto."""
    try:
        with open(archivo, "w") as f:
            materiales = sistema.listar_materiales()
            for mat in materiales:
                # Usar hasattr para diferenciar Libro de Recursos
                if hasattr(mat, 'get_isbn'):  # Es un Libro
                    linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_isbn()}|{mat.get_titulo()}|{mat.get_autor()}|{mat.get_año_publicacion()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
                else:  # Es un Recurso genérico
                    # Los recursos genéricos no tienen ISBN, Autor ni Año
                    linea = f"{mat.get_referencia()}|{mat.get_tipo()}|{mat.get_ejemplares_totales()}|{mat.get_ejemplares_disponibles()}\n"
                f.write(linea)
    except Exception as e:
        print(f"Error al guardar materiales: {e}")

def cargar_materiales(sistema, archivo="resources/data/materiales.txt"):
    """Carga los materiales guardados desde un archivo de texto."""
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                # Importamos aquí para evitar dependencia circular si no están importadas en el main
                from objetos.elemento import Libro, Recursos
                
                if len(partes) == 8: 
                    libro = Libro(partes[0], partes[1], partes[2], partes[3], 
                                  partes[4], int(partes[5]), int(partes[6]), int(partes[7]))
                    sistema.agregar_material(libro)
                elif len(partes) == 4: 
                    recurso = Recursos(partes[0], partes[1], int(partes[2]), int(partes[3]))
                    sistema.agregar_material(recurso)
    except FileNotFoundError:
        print("Archivo de materiales no encontrado. Iniciando con catálogo vacío.")
    except Exception as e:
        print(f"Error al cargar materiales: {e}")

# utilidades para guardar y cargar usuarios
def guardar_usuarios(sistema, archivo="resources/data/usuarios.txt"):
    with open(archivo, "w") as f:
        for usuario in sistema.usuarios.values():
            tipo = "Estudiante" if isinstance(usuario, Estudiante) else "Profesor"
            linea = f"{tipo}|{usuario.get_id()}|{usuario.get_nombre()}|{usuario.get_domicilio()}|{usuario.get_estado()}\n"
            f.write(linea)

def cargar_usuarios(sistema, archivo="resources/data/usuarios.txt"):
    try:
        with open(archivo, "r") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 5:
                    tipo, id_usuario, nombre, domicilio, estado = partes
                    if tipo == "Estudiante":
                        usuario = Estudiante(id_usuario, nombre, domicilio)
                    elif tipo == "Profesor":
                        usuario = Profesor(id_usuario, nombre, domicilio)
                    else:
                        continue
                    if estado == "suspendido":
                        usuario.suspender(0)  # Suspensión indefinida (puedes ajustar esto)
                    sistema.agregar_usuario(usuario)
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado. Iniciando con usuarios vacíos.")

