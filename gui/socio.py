# socio.py
import os

class Socio:
    def __init__(self, nombre, ci, correo):
        self.nombre = nombre
        self.ci = ci
        self.correo = correo
        self.tipo = "General"

    def to_line(self):
        return f"{self.tipo},{self.nombre},{self.ci},{self.correo}\n"


class Estudiante(Socio):
    def __init__(self, nombre, ci, correo, carrera):
        super().__init__(nombre, ci, correo)
        self.carrera = carrera
        self.tipo = "Estudiante"

    def to_line(self):
        return f"{self.tipo},{self.nombre},{self.ci},{self.correo},{self.carrera}\n"


class Profesor(Socio):
    def __init__(self, nombre, ci, correo, materia):
        super().__init__(nombre, ci, correo)
        self.materia = materia
        self.tipo = "Profesor"

    def to_line(self):
        return f"{self.tipo},{self.nombre},{self.ci},{self.correo},{self.materia}\n"


class GestorSocios:
    ARCHIVO = "socios.txt"

    @staticmethod
    def guardar(socio):
        with open(GestorSocios.ARCHIVO, "a", encoding="utf-8") as f:
            f.write(socio.to_line())

    @staticmethod
    def leer_todos():
        if not os.path.exists(GestorSocios.ARCHIVO):
            return []
        with open(GestorSocios.ARCHIVO, "r", encoding="utf-8") as f:
            return [line.strip().split(",") for line in f.readlines()]
