# app.py
from objetos.biblioteca import SistemaBiblioteca
from objetos.usuario import Estudiante, Profesor
from objetos.elemento import Libro, Recursos
from objetos.utilidades import guardar_materiales, cargar_materiales, guardar_usuarios, cargar_usuarios
from objetos.utilidades import Cola

reservas = {}  # Diccionario para manejar las colas de reservas

######### AGREGAR VALIDACIONES DESPUES #########

def menu_principal():
    sistema = SistemaBiblioteca()
    cargar_materiales(sistema)  # cargar datos existentes
    cargar_usuarios(sistema)
    print("Bienvenido al Sistema de Gestión de Biblioteca del CeRP")
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GESTIÓN DE BIBLIOTECA - CeRP")
        print("="*50)
        print("1. Gestión de Materiales")
        print("2. Gestión de Usuarios")
        print("3. Préstamos")
        print("4. Devoluciones")
        print("5. Consultar Catálogo")
        print("6. Usuarios en cola de espera")
        print("7. Guardar y Salir")
     # validaciones de entrada    
        opciones_validas = {"1","2","3","4","5","6","7"}
        opcion = ""
        while opcion not in opciones_validas:
            opcion = input("\nSeleccione opción: ")
            if opcion not in opciones_validas:
                print("opcion invalida. Intente nuevamente. ")

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
            print("\n--- Reservas ---")
            if not reservas:
                print("No hay reservas activas.")
            else:
                for titulo, cola in reservas.items():
                    print(f"Titulo/Material: {titulo}, en {cola}")
                    
        elif opcion == "7":
            guardar_usuarios(sistema)
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
    opciones_validas = {"1","2","3","4"}
    opcion = ""
    while opcion not in opciones_validas:
        opcion = input("Opcion: ")
        print("opcion invalida. Intente nuevamente. ")
    
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

    elif opcion == "2": 
        try:
            ref = input("Referencia (ej: REC001): ")
            tipo = input("Tipo de Recurso (ej: Cargador USB, Alargue): ")
            ejemplares = int(input("Ejemplares: "))
            
            recurso = Recursos(ref, tipo, ejemplares, ejemplares)
            sistema.agregar_material(recurso)
            print(f"Recurso '{tipo}' agregado")
        except ValueError:
             print("Error en los datos ingresados.Intente nuevamente.")

    elif opcion == "3":
        mostrar_catalogo(sistema)

    elif opcion == "4": # buscar por titulo o tipo
        buscar = input("Ingrese título/tipo para buscar: ") # ref = referencia de busqueda 
        material = sistema.buscar_material(buscar) # buscar por titulo o tipo de referencia
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
    
    if opcion == "1" or opcion == "2":
        tipo = "Estudiante" if opcion == "1" else "Profesor"
        id_usuario = input(f"ID del {tipo} (ej: EST001, PROF001): ")
        nombre = input("Nombre: ")
        domicilio = input("Domicilio: ")

        if opcion == "1":
            nuevo_usuario = Estudiante(id_usuario , nombre, domicilio)
        else:
           nuevo_usuario = Profesor(id_usuario , nombre, domicilio)
    
        sistema.agregar_usuario(nuevo_usuario)
        print(f" {tipo} '{nombre}' agregado.")

    
    elif opcion == "3":
        print("\n-- USUARIOS REGISTRADOS ---")
        if not sistema.usuarios:
            print("no hay usuarios.")
        for usuario in sistema.usuarios.values():
            print(f" {usuario}")

def menu_prestamos(sistema):
    print("\n--- REALIZAR PRÉSTAMO ---")
    id_usuario = input("ID del usuario: ")
    titulo = input("Titulo o Tipo del material: ")
    
    exito, msg, prestamo = sistema.realizar_prestamo(id_usuario, titulo)
    print(f"Resultado: {msg}")

#si se realizo bien el prestamo mostrara la fecha
    if exito and prestamo is not None:
        print(f"Fecha de venciminto del prestamo: {prestamo.fecha_prestamo}")
        print(f"fecha estimada de devolucion: {prestamo.fecha_devolucion}")     
        
 #cola de espera si no hay ejemplares disponibles  
    if not exito and "no disponible"in msg.lower():
        if titulo not in reservas:
            reservas[titulo] = Cola()

        cola = reservas[titulo]
        if not cola.contiene(id_usuario):
            cola. encolar(id_usuario)
            print(f"No hay ejemplares disponibles. El usuario fue agregado a la cola de espera")
            print(f"Posición en la cola: {cola.tamanio()}")
        else:
            print("el usuario ya está en la cola de espera para este material.")
            
            
def menu_devoluciones(sistema):
    print("\n--- REALIZAR DEVOLUCIÓN ---")
    id_usuario = input("ID del usuario: ")
    titulo = input("Titulo o Tipo del material: ")

    exito, msg, fecha_devolucion = sistema.realizar_devolucion(id_usuario, titulo)
    print(f"Resultado: {msg}")
    
    if exito:
        print(f"fecha de devolucion:",{fecha_devolucion})
    
    if titulo in reservas and not reservas [titulo].estaVacia():
        siguiente_usuario = reservas[titulo].desencolar()
        print(f"El siguiente usuario en la cola es: {siguiente_usuario}")
        exito, msg2 = sistema.realizar_prestamo(siguiente_usuario, titulo)
        print(f"Resultado del préstamo al siguiente usuario: {msg2}")
        
        if reservas[titulo].estaVacia():
            del reservas[titulo]

def mostrar_catalogo(sistema):
    print("\n--- CATÁLOGO DE MATERIALES ---")
    materiales = sistema.listar_materiales()

    if not materiales:
        print("No hay materiales registrados.")
    else:
        for mat in materiales:
            print(f"  {mat}")


if __name__ == "__main__":
    menu_principal()