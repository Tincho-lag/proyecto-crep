# app.py

from objetos.biblioteca import SistemaBiblioteca
from objetos.usuario import Estudiante, Profesor
from objetos.elemento import Libro, Recursos
from objetos.utilidades import (
    guardar_materiales, cargar_materiales,
    guardar_usuarios, cargar_usuarios,
    guardar_prestamos, cargar_prestamos,
    guardar_reservas, cargar_reservas,
    Cola
)

def menu_principal():
    # menu principal del sistema de biblioteca
    # inicializar sistema y cargar datos persistentes
    sistema = SistemaBiblioteca()
    cargar_materiales(sistema)
    cargar_usuarios(sistema)
    cargar_prestamos(sistema)
    cargar_reservas(sistema)
    
    print("bienvenido al sistema de gestion de biblioteca del cerp\n")
    
    while True:
        print("\n" + "="*50)
        print("sistema de gestion de biblioteca - cerp")
        print("="*50)
        print("1. gestion de materiales")
        print("2. gestion de usuarios")
        print("3. prestamos")
        print("4. devoluciones")
        print("5. consultar catalogo")
        print("6. ver reservas activas")
        print("7. ver transacciones")
        print("8. guardar y salir")
        
        # validacion de entrada
        opciones_validas = {"1", "2", "3", "4", "5", "6", "7", "8"}
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
            mostrar_reservas(sistema)
        elif opcion == "7":
            mostrar_transacciones()
        elif opcion == "8":
            # guardar todos los datos antes de salir
            guardar_materiales(sistema)
            guardar_usuarios(sistema)
            guardar_prestamos(sistema)
            guardar_reservas(sistema)
            print("\ndatos guardados. hasta luego!")
            break


def menu_materiales(sistema):
    # submenu para gestion de materiales
    print("\n--- gestion de materiales ---")
    print("1. agregar libro")
    print("2. agregar recurso generico")
    print("3. listar todos")
    print("4. buscar por titulo")
    
    opciones_validas = {"1", "2", "3", "4"}
    opcion = ""
    
    while opcion not in opciones_validas:
        opcion = input("opcion: ")
        if opcion not in opciones_validas:
            print("opcion invalida.")
    
    if opcion == "1":
        # agregar libro con validacion de datos
        try:
            ref = input("referencia: ")
            isbn = input("isbn: ")
            titulo = input("titulo: ").strip()
            autor = input("autor: ")
            ano = int(input("ano publicacion: "))
            ejemplares = int(input("ejemplares: "))
            
            libro = Libro(ref, "libro", isbn, titulo, autor, ano, ejemplares, ejemplares)
            sistema.agregar_material(libro)
            print("✓ libro agregado exitosamente")
        
        except ValueError:
            print("error: datos invalidos. intente nuevamente.")

    elif opcion == "2":
        # agregar recurso generico
        try:
            ref = input("referencia (ej: rec001): ")
            tipo = input("tipo (ej: cargador, revista): ").strip()
            ejemplares = int(input("ejemplares: "))
            
            recurso = Recursos(ref, tipo, ejemplares, ejemplares)
            sistema.agregar_material(recurso)
            print(f"✓ recurso '{tipo}' agregado exitosamente")
        
        except ValueError:
            print("error: datos invalidos. intente nuevamente.")

    elif opcion == "3":
        mostrar_catalogo(sistema)

    elif opcion == "4":
        # buscar material por titulo
        buscar = input("ingrese titulo/tipo: ").strip()
        material = sistema.buscar_material(buscar)
        
        if material:
            print(f"\n✓ material encontrado:\n  {material}")
        else:
            print("✗ material no encontrado.")


def menu_usuarios(sistema):
    # submenu para gestion de usuarios
    print("\n--- gestion de usuarios ---")
    print("1. agregar estudiante")
    print("2. agregar profesor")
    print("3. listar todos")
    
    opcion = input("opcion: ")
    
    if opcion == "1" or opcion == "2":
        tipo = "estudiante" if opcion == "1" else "profesor"
        id_usuario = input(f"id del {tipo}: ")
        nombre = input("nombre: ")
        domicilio = input("domicilio: ")
        
        # crear usuario segun tipo
        if opcion == "1":
            nuevo_usuario = Estudiante(id_usuario, nombre, domicilio)
        else:
            nuevo_usuario = Profesor(id_usuario, nombre, domicilio)
        
        sistema.agregar_usuario(nuevo_usuario)
        print(f"✓ {tipo} '{nombre}' agregado exitosamente")
    
    elif opcion == "3":
        print("\n--- usuarios registrados ---")
        if not sistema.usuarios:
            print("no hay usuarios registrados.")
        else:
            for usuario in sistema.usuarios.values():
                print(f"  {usuario}")


def menu_prestamos(sistema):
    # procesa solicitudes de prestamo
    print("\n--- realizar prestamo ---")
    id_usuario = input("id del usuario: ")
    titulo = input("titulo del material: ").strip()
    
    # intentar realizar prestamo
    exito, msg, prestamo = sistema.realizar_prestamo(id_usuario, titulo)
    print(f"\nresultado: {msg}")
    
    # mostrar detalles si fue exitoso
    if exito and prestamo is not None:
        print(f"fecha prestamo: {prestamo.get_fecha_prestamo().strftime('%d/%m/%Y %H:%M')}")
        print(f"fecha vencimiento: {prestamo.get_fecha_vencimiento().strftime('%d/%m/%Y')}")
    
    # agregar a cola si no hay disponibilidad
    elif not exito and "no disponible" in msg.lower():
        if titulo not in sistema.reservas:
            sistema.reservas[titulo] = Cola()
        
        cola = sistema.reservas[titulo]
        
        if not cola.contiene(id_usuario):
            cola.encolar(id_usuario)
            print(f"\n→ usuario agregado a cola de espera")
            print(f"  posicion: {cola.tamanio()}")
        else:
            print("→ usuario ya esta en cola de espera")


def menu_devoluciones(sistema):
    # procesa devoluciones de materiales
    print("\n--- realizar devolucion ---")
    id_usuario = input("id del usuario: ")
    titulo = input("titulo del material: ").strip()
    
    # procesar devolucion
    exito, msg = sistema.realizar_devolucion(id_usuario, titulo)
    print(f"\nresultado: {msg}")


def mostrar_catalogo(sistema):
    # muestra todos los materiales ordenados alfabeticamente
    print("\n--- catalogo de materiales ---")
    materiales = sistema.listar_materiales()
    
    if not materiales:
        print("no hay materiales registrados.")
    else:
        for i, mat in enumerate(materiales, 1):
            print(f"  {i}. {mat}")
        print(f"\ntotal: {len(materiales)} materiales")


def mostrar_reservas(sistema):
    # muestra todas las colas de espera activas
    print("\n--- reservas activas ---")
    
    if not sistema.reservas:
        print("no hay reservas activas.")
    else:
        for titulo, cola in sistema.reservas.items():
            print(f"\nmaterial: {titulo}")
            print(f"  usuarios en espera: {cola.tamanio()}")
            print(f"  cola: {cola}")


def mostrar_transacciones():
    # muestra el historial de transacciones
    print("\n--- historial de transacciones ---")
    
    try:
        with open("resources/data/transacciones.txt", "r") as f:
            lineas = f.readlines()
            
            if not lineas:
                print("no hay transacciones registradas.")
                return
            
            # mostrar ultimas 30 transacciones
            print(f"mostrando ultimas {min(30, len(lineas))} transacciones:\n")
            
            for linea in lineas[-30:]:
                print(f"  {linea.strip()}")
            
            print(f"\ntotal de transacciones: {len(lineas)}")
    
    except FileNotFoundError:
        print("no hay transacciones registradas aun.")
    except Exception as e:
        print(f"error al leer transacciones: {e}")


if __name__ == "__main__":
    menu_principal()