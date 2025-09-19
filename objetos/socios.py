# objetos/socios.py 
from objetos.usuario import Usuario

class Estudiante(Usuario): # hereda de usuario puede ver libros y socilitar prestamos
    def __init__(self, id, nombre, domicilio):
        super().__init__(id, nombre, domicilio,)
        self.__tipo = "Estudiante"


class Profesor(Usuario): # hereda de usuario puede ver libros y solicitar prestamos
    def __init__(self, id, nombre, domicilio,):
        super().__init__(id , nombre, domicilio)
        self.__tipo = "Profesor"

    