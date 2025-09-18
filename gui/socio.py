import os

 #_____Aca difinimos la funcion  generar_id_simple______(archivo="socios.txt") es decirle a la función dónde buscar los IDs existentes para poder calcular el siguiente.
def generar_id_simple(archivo="socios.txt"):
#____Esto sirve para prevenir errores: el código dentro del try se intenta ejecutar normalmente, y si ocurre un error, se salta al bloque except
    try:
#____ Esto es pra que el usuario no tenga que crear el ID manualmente, si no existe, se crea automaticamente
        with open(archivo, "r", encoding="utf-8") as f:
#______Lee todas las líneas del archivo y las guarda en la lista lineas, cada elemento de la lista es una línea del archivo, normalmente con información de un socio, como "nombre,ID,correo"
            lineas = f.readlines()  
            
#______Verifica si esta vacío y si el archivo está vacío (no hay datos), devuelve "001" como el primer ID.
            if not lineas:
                return "001"  
#__________________Estas lineas  (lineas[-1]) = toma la última línea del archivo, es decir, el último socio registrado.
#________________________________(.strip()) = elimina espacios o saltos de línea al inicio o al final.
#________________________________(.split("-")) = divide la línea en partes separadas por comas, generando una lista
            ultimo = lineas[-1].strip().split(",")[1]  
         #___Convierte el último ID a un número entero con int() y le suma 1 para generar el siguiente ID en secuencia.
            nuevo_id = int(ultimo) + 1
        #___Convierte el nuevo ID de vuelta a cadena con str() y el (.zfill(3) = asegura que tenga 3 dígitos
            return str(nuevo_id).zfill(3)
    #____ Si el archivo no existe, devuelve "001" como el primer ID.
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
#______El -line.split("-")- divide cada dato de los socios en una lista separada por un guieon(,).
#El -i.readlines()- lee todas las líneas del archivo en una lista.
            return [line.strip().split(",") for line in i.readlines()]
