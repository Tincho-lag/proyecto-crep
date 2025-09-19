from typing import List, Optional

class Administrador:
    """Administrador (mínimo, solo ID y nombre por ahora)."""
    def __init__(self, id: str, nombre: str):
        self._id = id
        self._nombre = nombre

    def __repr__(self):
        return f"Administrador(id={self._id!r}, nombre={self._nombre!r})"


class Usuario:
    """Clase base para todos los usuarios."""
    def __init__(self, id: str, nombre: str, domicilio: str, 
                 material_prestado: Optional[List[str]] = None, 
                 estado: str = "activo"):
        self._id = id
        self._nombre = nombre
        self._domicilio = domicilio
        self._material_prestado = material_prestado if material_prestado is not None else []
        self._estado = estado  # "activo" o "suspendido"

    # --- getters ---
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_domicilio(self):
        return self._domicilio

    def get_estado(self):
        return self._estado

    def get_material_prestado(self):
        return self._material_prestado

    # --- setters ---
    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def set_domicilio(self, domicilio: str):
        self._domicilio = domicilio

    def set_estado(self, estado: str):
        self._estado = estado

    # --- métodos ---
    def prestar_material(self, material: str):
        self._material_prestado.append(material)

    def devolver_material(self, material: str):
        if material in self._material_prestado:
            self._material_prestado.remove(material)


class Estudiante(Usuario):
    def __init__(self, id: str, nombre: str, domicilio: str, carrera: str):
        super().__init__(id, nombre, domicilio)
        self.carrera = carrera

    def __repr__(self):
        return f"Estudiante(id={self._id!r}, nombre={self._nombre!r}, carrera={self.carrera!r})"


class Profesor(Usuario):
    def __init__(self, id: str, nombre: str, domicilio: str, materia: str):
        super().__init__(id, nombre, domicilio)
        self.materia = materia

    def __repr__(self):
        return f"Profesor(id={self._id!r}, nombre={self._nombre!r}, materia={self.materia!r})"
