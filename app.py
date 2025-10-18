from objetos.biblioteca import SistemaBiblioteca
from objetos.usuario import Estudiante, Profesor
from objetos.elemento import Libro, Recursos
from objetos.utilidades import guardar_materiales, cargar_materiales, guardar_usuarios, cargar_usuarios
from objetos.utilidades import Cola, guardar_prestamos, cargar_prestamos, guardar_reservas, cargar_reservas, registrar_historial

# agregar validaciones despues
def menu_principal():
    sistema = SistemaBiblioteca()
    cargar_materiales(sistema)  # cargar datos existentes
    cargar_usuarios(sistema)
    cargar_prestamos(sistema)
    cargar_reservas(sistema)
    print("bienvenido al sistema de gestion de biblioteca del cerp")
    
    while True:
        print("\n" + "="*50)
        print("sistema de gestion de biblioteca - cerp")
        print("="*50)
        print("1. gestion de materiales")
        print("2. gestion de usuarios")
        print("3. prestamos")
        print("4. devoluciones")
        print("5. consultar catalogo")
        print("6. usuarios en cola de espera")
        print("7. guardar y salir")
        # validaciones de entrada    
        opciones_validas = {"1","2","3","4","5","6","7"}
        opcion = ""
        while opcion not in opciones_validas:
            opcion = input("\nseleccione opcion: ")
            if opcion not in opciones_validas:
                print("opcion invalida. intente nuevamente.")

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
            print("\n--- reservas ---")
            if not sistema.reservas:
                print("no hay reservas activas.")
            else:
                for titulo, cola in sistema.reservas.items():
                    print(f"titulo/material: {titulo}, en {cola}")
        elif opcion == "7":
            guardar_usuarios(sistema)
            guardar_materiales(sistema)
            guardar_prestamos(sistema)
            guardar_reservas(sistema)
            print("datos guardados. hasta luego!")
            break

def menu_materiales(sistema):
    print("\n--- gestion de materiales ---")
    print("1. agregar libro (con isbn, titulo, autor)")
    print("2. agregar recurso (generico, ej: cargador, revista, comic etc)")
    print("3. listar todos")
    print("4. buscar por titulo/tipo")
    opciones_validas = {"1","2","3","4"}
    opcion = ""
    while opcion not in opciones_validas:
        opcion = input("opcion: ")
    
    if opcion == "1":
        try:
            ref = input("referencia: ")
            isbn = input("isbn: ")
            titulo = input("titulo: ").strip()
            autor = input("autor: ")
            ano = int(input("ano publicacion: "))
            ejemplares = int(input("ejemplares: "))
        
            libro = Libro(ref, "libro", isbn, titulo, autor, ano, ejemplares, ejemplares)
            sistema.agregar_material(libro)
            print("libro agregado")
        except ValueError:
            print("error en los datos ingresados. intente nuevamente.")

    elif opcion == "2": 
        try:
            ref = input("referencia (ej: rec001): ")
            tipo = input("tipo de recurso (ej: cargador usb, alargue): ").strip()
            ejemplares = int(input("ejemplares: "))
            
            recurso = Recursos(ref, tipo, ejemplares, ejemplares)
            sistema.agregar_material(recurso)
            print(f"recurso '{tipo}' agregado")
        except ValueError:
            print("error en los datos ingresados. intente nuevamente.")

    elif opcion == "3":
        mostrar_catalogo(sistema)

    elif opcion == "4":
        buscar = input("ingrese titulo/tipo para buscar: ").strip()
        material = sistema.buscar_material(buscar)
        if material:
            print(f"material encontrado: {material}")
        else:
            print("material no encontrado.")

def menu_usuarios(sistema):
    print("\n--- gestion de usuarios ---")
    print("1. agregar estudiante")
    print("2. agregar profesor")
    print("3. listar todos")
    opcion = input("opcion: ")
    
    if opcion == "1" or opcion == "2":
        tipo = "estudiante" if opcion == "1" else "profesor"
        id_usuario = input(f"id del {tipo} (ej: est001, prof001): ")
        nombre = input("nombre: ")
        domicilio = input("domicilio: ")
        if opcion == "1":
            nuevo_usuario = Estudiante(id_usuario, nombre, domicilio)
        else:
            nuevo_usuario = Profesor(id_usuario, nombre, domicilio)
    
        sistema.agregar_usuario(nuevo_usuario)
        print(f"{tipo} '{nombre}' agregado.")
    
    elif opcion == "3":
        print("\n--- usuarios registrados ---")
        if not sistema.usuarios:
            print("no hay usuarios.")
        for usuario in sistema.usuarios.values():
            print(f"{usuario}")

def menu_prestamos(sistema):
    print("\n--- realizar prestamo ---")
    id_usuario = input("id del usuario: ")
    titulo = input("titulo o tipo del material: ").strip()
    
    exito, msg, prestamo = sistema.realizar_prestamo(id_usuario, titulo)
    print(f"resultado: {msg}")
    if exito and prestamo is not None:
        print(f"fecha de prestamo: {prestamo.get_fecha_prestamo().strftime('%d/%m/%Y %H:%M')}")
        print(f"fecha estimada de devolucion: {prestamo.get_fecha_vencimiento().strftime('%d/%m/%Y')}")
        registrar_historial("prestamo", prestamo.get_usuario(), prestamo.get_material())
    
    # cola de espera si no hay ejemplares disponibles  
    if not exito and "no disponible" in msg.lower():
        if titulo not in sistema.reservas:
            sistema.reservas[titulo] = Cola()
        cola = sistema.reservas[titulo]
        if not cola.contiene(id_usuario):
            cola.encolar(id_usuario)
            print(f"no hay ejemplares disponibles. el usuario fue agregado a la cola de espera")
            print(f"posicion en la cola: {cola.tamanio()}")
        else:
            print("el usuario ya esta en la cola de espera para este material.")

def menu_devoluciones(sistema):
    print("\n--- realizar devolucion ---")
    id_usuario = input("id del usuario: ")
    titulo = input("titulo o tipo del material: ").strip()
    # para probar retrasos, mockear datetime.now() sumando dias manualmente
    # from unittest.mock import patch
    # from datetime import datetime, timedelta
    # with patch('datetime.datetime.now') as mock_now:
    #     mock_now.return_value = datetime.now() + timedelta(days=3)  # simular 3 dias de retraso
    #     exito, msg = sistema.realizar_devolucion(id_usuario, titulo)
    #     print(f"resultado: {msg}")
    #     return
    exito, msg = sistema.realizar_devolucion(id_usuario, titulo)
    print(f"resultado: {msg}")
    if exito:
        material = sistema.buscar_material(titulo)
        if material:
            registrar_historial("devolucion", sistema.usuarios.get(id_usuario), material)

def mostrar_catalogo(sistema):
    print("\n--- catalogo de materiales ---")
    materiales = sistema.listar_materiales()
    if not materiales:
        print("no hay materiales registrados.")
    else:
        for mat in materiales:
            print(f"  {mat}")

if __name__ == "__main__":
    menu_principal()