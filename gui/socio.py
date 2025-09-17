import os

# --- Generar ID automático ---
def generar_id_simple(archivo="socios.txt"):
    """Genera un ID automático secuencial (001, 002, 003, ...)"""
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if not lineas:
                return "001"  # Primer socio
            ultimo = lineas[-1].strip().split(",")[1]  # El ID está en la posición 1
            nuevo_id = int(ultimo) + 1
            return str(nuevo_id).zfill(3)
    except FileNotFoundError:
        return "001"

#________________________________Clases de Registro y gestor de socios_____________________________________
#__________________________Gestor de Socios, donde se guarda todos los  datos de los socios
# En las clases socio, estudiante y profesor, representan los diferentes tipos de socios y sus datos
#   Cada clase tiene un metodo -"to_line()"- convierte los datos de los socios en una línea de texto para guardarlos en un archivo.
# _____________________________________
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
        return f"{self.tipo},{self.id},{self.nombre},{self.ci},{self.correo},{self.domicilio},{self.observaciones}\n"

class Estudiante(Socio):
    def __init__(self, id, nombre, ci, correo, carrera, domicilio, observaciones):
        super().__init__(id, nombre, ci, correo, domicilio, observaciones)
        self.carrera = carrera
        self.tipo = "Estudiante"

    def to_line(self):
        return f"{self.tipo},{self.id},{self.nombre},{self.ci},{self.correo},{self.carrera},{self.domicilio},{self.observaciones}\n"

class Profesor(Socio):
    def __init__(self, id, nombre, ci, correo, materia, domicilio, observaciones):
        super().__init__(id, nombre, ci, correo, domicilio, observaciones)
        self.materia = materia
        self.tipo = "Profesor"

    def to_line(self):
        return f"{self.tipo},{self.id},{self.nombre},{self.ci},{self.correo},{self.materia},{self.domicilio},{self.observaciones}\n"
    
    
#______________________________________La clase GestorSocios se encarga de guardar esos datos en un archivo (socios.txt) para luego leerlos.
class GestorSocios:
    def __init__(self, archivo="socios.txt"):
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
#______El -line.split("-")- divide cada dato de los socios en una lista separada por un guieon(-).
#El -i.readlines()- lee todas las líneas del archivo en una lista.
            return [line.strip().split("-") for line in i.readlines()]
