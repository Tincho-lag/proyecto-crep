import os
from gui.registro_socios import generar_id, agregar_socio

DATA_DIR = os.path.join(os.path.dirname(__file__), "../resources/data")
os.makedirs(DATA_DIR, exist_ok=True)
ARCHIVO_SOCIOS = os.path.join(DATA_DIR, "socios.txt")

1

 #_____Aca difinimos la funcion  generar_id_simple______(archivo="socios.txt") es decirle a la función dónde buscar los IDs existentes para poder calcular el siguiente.
def generar_id_simple(archivo=ARCHIVO_SOCIOS):
#____Esto sirve para prevenir errores: el código dentro del try se intenta ejecutar normalmente, y si ocurre un error, se salta al bloque except
    try:
#____ Esto es pra que el usuario no tenga que crear el ID manualmente, si no existe, se crea automaticamente
        with open(archivo, "r", encoding="utf-8") as f:
            
        #___Lo que hace es leer cada line del archivo f.
        #___(.strip()) = elimina espacios o saltos de línea al inicio o al final.
#___________(.split("-")) = divide la línea en partes separadas por comas, generando una lista
            lineas = [line.strip() for line in f if line.strip()]
#____Aquí se verifica si lineas está vacío (es decir, no había socios en el archivo) y si no hay registros, significa que es el primer socio, por lo tanto devuelve "001"         
            if not lineas:
                return "001"
        #___Recorre las líneas en orden inverso (desde la última hasta la primera) para encontrar el ID más alto.
        #___Esto es eficiente porque el ID más alto suele estar al final del archivo.
            for linea in reversed(lineas):
                #___Separa la línea en partes usando la coma como delimitador.
                partes = linea.split(",")
                if len(partes) > 0 and partes[0].isdigit():
                #___Convierte el último ID a un número entero con int() y le suma 1 para generar el siguiente ID en secuencia.
                    nuevo_id = int(partes[0]) + 1
                #___Convierte el nuevo ID de vuelta a cadena con str() y el (.zfill(3) = asegura que tenga 3 dígitos
                    return str(nuevo_id).zfill(3)
            return "001"
    #____ Si el archivo no existe, devuelve "001" como el primer ID.
    except FileNotFoundError:
        return "001"

class Socio:
    def __init__(self, id, nombre, ci, correo, domicilio, observaciones):
        self.id = id
        self.nombre = nombre
        self.ci = ci
        self.correo = correo
        self.domicilio = domicilio
        self.observaciones = observaciones
        self.tipo = "General"

    def to_line(self):
        return f"{self.id},{self.tipo},{self.nombre},{self.ci},{self.correo},{self.domicilio},{self.observaciones}\n"

class Estudiante(Socio):
    def __init__(self, id, nombre, ci, correo, carrera, domicilio, observaciones):
        super().__init__(id, nombre, ci, correo, domicilio, observaciones)
        self.carrera = carrera
        self.tipo = "Estudiante"

    def to_line(self):
        return f"{self.id},{self.tipo},{self.nombre},{self.ci},{self.correo},{self.carrera},{self.domicilio},{self.observaciones}\n"

class Profesor(Socio):
    def __init__(self, id, nombre, ci, correo, materia, domicilio, observaciones):
        super().__init__(id, nombre, ci, correo, domicilio, observaciones)
        self.materia = materia
        self.tipo = "Profesor"

    def to_line(self):
        return f"{self.id},{self.tipo},{self.nombre},{self.ci},{self.correo},{self.materia},{self.domicilio},{self.observaciones}\n"

#______________________________________La clase GestorSocios se encarga de guardar esos datos en un archivo (socios.txt) para luego leerlos.
class GestorSocios:
    def __init__(self, archivo=ARCHIVO_SOCIOS):
        self.archivo = archivo
        
#__________________El metodo  "guardar()" abre el archivo en modo append y escribe la línea.______________________________
    def guardar(self, socio):
        
#______________________________________________Esta linea  "with open(...) as i:" y la asocia con la variable "i" 
# Python usa modos de archivo de una letra para que sea más corto y simple ("a" → append (agregar al final)).
# Si pusieras "append", Python no lo entendería porque solo reconoce las letras definidas.
# esto hace que el socio no se sobrescriba y vaya al siguiente____________________
        with open(self.archivo, "a", encoding="utf-8") as i:
            
#___________escribe la línea de texto del socio en el archivo.
            i.write(socio.to_line())

#__________________El metodo "leer_todos()" abre el archivo en modo lectura y lee todas las líneas, devolviendo una lista de listas.________________
    def leer_todos(self):
#______________Verifica si el archivo existe. Si no existe, devuelve una lista vacía ([]) para evitar errores.___________________
        if not os.path.exists(self.archivo):
            return []
        
#_________________________Abre el archivo en modo lectura ("r")
        with open(self.archivo, "r", encoding="utf-8") as i:
#______El -line.strip()- elimina espacios en blanco y saltos de línea al inicio y final de cada línea.
#______El -line.split("-")- divide cada dato de los socios en una lista separada por un guieon(,).
#El -i.readlines()- lee todas las líneas del archivo en una lista.
            return [line.strip().split(",") for line in i.readlines()]


#Se ejecuta en la terminal con: pytest tests/test_socio.py
if __name__ == "__main__":
    gestor = GestorSocios()

    print("=== Sistema de Registro de Socios (modo terminal) ===\n")

    while True:
        print("Opciones:")
        print("1. Registrar nuevo socio")
        print("2. Ver lista de socios")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            id_nuevo = generar_id_simple()
            nombre = input("Nombre: ")
            ci = input("Cédula: ")
            correo = input("Correo: ")
            domicilio = input("Domicilio: ")
            observaciones = input("Observaciones: ")

            tipo = input("Tipo (G=General, E=Estudiante, P=Profesor): ").upper()
            if tipo == "E":
                carrera = input("Carrera: ")
                socio = Estudiante(id_nuevo, nombre, ci, correo, carrera, domicilio, observaciones)
            elif tipo == "P":
                materia = input("Materia: ")
                socio = Profesor(id_nuevo, nombre, ci, correo, materia, domicilio, observaciones)
            else:
                socio = Socio(id_nuevo, nombre, ci, correo, domicilio, observaciones)

            gestor.guardar(socio)
            print(f"\n Socio '{nombre}' registrado con ID {id_nuevo}\n")

        elif opcion == "2":
            socios = gestor.leer_todos()
            if not socios:
                print("\nNo hay socios registrados.\n")
            else:
                print("\n=== Lista de Socios ===")
                for s in socios:
                    print(", ".join(s))
                print()

        elif opcion == "3":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpción inválida. Intente de nuevo.\n")
