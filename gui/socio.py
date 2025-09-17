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

# --- Clases ---
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

class GestorSocios:
    def __init__(self, archivo="socios.txt"):
        self.archivo = archivo

    def guardar(self, socio):
        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(socio.to_line())

    def leer_todos(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, "r", encoding="utf-8") as f:
            return [line.strip().split("-") for line in f.readlines()]
