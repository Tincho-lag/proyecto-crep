# app.py
from objetos.biblioteca import SistemaBiblioteca, guardar_materiales, cargar_materiales
from objetos.elemento import Libro, Recursos
from objetos.usuario import Estudiante, Profesor

def menu_principal():
    sistema = SistemaBiblioteca()
    cargar_materiales(sistema)  # Cargar datos existentes
    sistema.agregar_usuario(Estudiante("EST001", "Ana García", "Tacuarembó 123"))
    sistema.agregar_usuario(Profesor("PROF001", "Dr. Juan Pérez", "Rivera 456"))

    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GESTIÓN DE BIBLIOTECA - CeRP")
        print("="*50)
        print("1. Gestión de Materiales")
        print("2. Gestión de Usuarios")
        print("3. Préstamos")
        print("4. Devoluciones")
        print("5. Consultar Catálogo")
        print("6. Guardar y Salir")
        
        opcion = input("\nSeleccione opción: ")
        
        if opcion == "1":
            menu_materiales(sistema)
        elif opcion == "2":
            menu_usuarios(sistema)
        elif opcion == "3":
            menu_prestamos(sistema)
        elif opcion == "4":
            menu_devoluciones(sistema)
        elif opcion == "5":
            mostrar_catalogo(sistema)
        elif opcion == "6":
            guardar_materiales(sistema)
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_materiales(sistema):
    print("\n--- GESTIÓN DE MATERIALES ---")
    print("1. Agregar Libro (con ISBN, Título, Autor)")
    print("2. Agregar Recurso (genérico, ej: Cargador , Revista, Comic etc)")
    print("3. Listar todos")
    print("4. Buscar por titulo/tipo")
    opcion = input("Opción: ")
    
    if opcion == "1":
        try:
            ref = input("Referencia: ")
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            año = int(input("Año publicación: "))
            ejemplares = int(input("Ejemplares: "))
        
            libro = Libro(ref, "Libro", isbn, titulo, autor, año, ejemplares, ejemplares)
            sistema.agregar_material(libro)
        except ValueError:
            print("Error en los datos ingresados. Intente nuevamente.")
        print(" Libro agregado")

    elif opcion == "2": # agregar Recurso Genérico
        try:
            ref = input("Referencia (ej: REC001): ")
            tipo = input("Tipo de Recurso (ej: Cargador USB, Alargue 5m): ")
            ejemplares = int(input("Ejemplares: "))
            
            recurso = Recursos(ref, tipo, ejemplares, ejemplares)
            sistema.agregar_material(recurso)
            print(f"Recurso '{tipo}' agregado")
        except ValueError:
             print("Error en los datos ingresados. Intente nuevamente.")

    elif opcion == "3":
        mostrar_catalogo(sistema)

    elif opcion == "4": # buscar por titulo o tipo
        ref = input("Ingrese título o tipo a buscar: ") # ref = referencia de busqueda 
        material = sistema.buscar_material(ref) # buscar por titulo o tipo de referencia
        if material:
            print(f"Material encontrado: {material}")
        else:
            print("Material no encontrado.")
def menu_usuarios(sistema):
    print("\n--- GESTIÓN DE USUARIOS ---")
    print("1. Agregar Estudiante")
    print("2. Agregar Profesor")
    print("3. Listar todos")
    opcion = input("Opción: ")
    
    if opcion == "1":
        id = input("ID (ej: EST001): ")
        nombre = input("Nombre: ")
        domicilio = input("Domicilio: ")
        estudiante = Estudiante(id, nombre, domicilio)
        sistema.agregar_usuario(estudiante)
        print(f"Estudiante '{nombre}' agregado.")
    
    elif opcion == "2":
        id = input("ID (ej: PROF001): ")
        nombre = input("Nombre: ")
        domicilio = input("Domicilio: ")
        profesor = Profesor(id, nombre, domicilio)
        sistema.agregar_usuario(profesor)
        print(f"Profesor '{nombre}' agregado.")
    
    elif opcion == "3":
        print("\n--- LISTA DE USUARIOS ---")
        for usuario in sistema.usuarios.values():
            print(f"  {usuario}")

def menu_prestamos(sistema):
    print("\n--- REALIZAR PRÉSTAMO ---")
    id_usuario = input("ID del usuario: ")
    titulo = input("Título del material: ")
    
    exito, msg = sistema.realizar_prestamo(id_usuario, titulo)
    print(f"Resultado: {msg}")

def mostrar_catalogo(sistema):
    print("\n--- CATÁLOGO DE MATERIALES ---")
    for mat in sistema.listar_materiales():
        print(f"  {mat}")

if __name__ == "__main__":
    menu_principal()