import os

class Socio:
    def __init__(self, nombre, ci, correo):
        if not ci.isdigit():
            raise ValueError("La cédula debe contener solo números")

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
    def __init__(self, archivo="socios.txt"):
        self.archivo = archivo

    def guardar(self, socio):
        """Guarda un socio en el archivo"""
        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(socio.to_line())

    def leer_todos(self):
        """Lee todos los socios desde el archivo"""
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, "r", encoding="utf-8") as f:
            return [line.strip().split(",") for line in f.readlines()]
