# objetos/socios.py 
from objetos.usuario import Usuario

class Estudiante(Usuario): # hereda de usuario puede ver libros y socilitar prestamos
    def __init__(self, id, nombre, domicilio, material_prestado, estado, suspencion, carrera, tipo ):
        super().__init__(id, nombre, domicilio, material_prestado , estado)
        self.__suspencion = suspencion
        self.__carrera = carrera
        self.__tipo = "Estudiante"

class Profesor(Usuario): # hereda de usuario puede ver libros y solicitar prestamos
    def __init__(self, id, nombre, domicilio, material_prestado, estado, suspencion, carrera, tipo ):
        super().__init__(id , nombre, domicilio, material_prestado)
        self.__tipo = "Profesor"

    # setters
    def set_suspencion(self, suspencion):
        self.__suspencion = suspencion

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def get_tipo(self, tipo):
        self.__tipo = tipo 