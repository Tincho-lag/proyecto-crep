# usuario.py

class Administrador:  # desarrollar luego (no usado por ahora) se supone que puede agregar o eliminar usuarios
    def __init__(self, id, nombre, ):
        self.__id = id
        self.__nombre = nombre

class Usuario: # clase base
    def __init__(self, id, nombre, domicilio, material_prestado = []):
        self.__id = id
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__material_prestado = []  #lista para rastrear materiales prestados
        self.__estado = None # por defecto activo con string "activo"
        self.__suspencion = None # poner fecha de suspencion
        self.__tipo = None  

class Estudiante(Usuario): # hereda de usuario puede ver libros y socilitar prestamos
    def __init__(self, id, nombre, domicilio, carrera, tipo, material_prestado = None ): 
        super().__init__(carrera, tipo)
        self.__carrera = carrera
        self.__tipo = "Estudiante"

class Profesor(Usuario): # hereda de usuario puede ver libros y solicitar prestamos
    def __init__(self, id, nombre, domicilio, carrera, tipo, material_prestado = None ):
        super().__init__(id , nombre, domicilio, material_prestado)
        self.__tipo = "Profesor"

    # setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio
    def set_carrera(self, carrera):
        self.__carrera = carrera
    def set_tipo(self, tipo):
        self.__tipo = tipo 
    def material_prestado (): # lista prestamos del usuario incompleta no se como hacerla

    # getters
    def get_id_socio(self):
        return self.__id_socio

    def get_nombre(self):
        return self.__nombre

    def get_material_prestado(self):
        return self.__material_prestado

    # setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
        self.__telefono = telefono




#biblioteca_sistema 

# Estructura del proyecto:
#├── models/a
#│   ├────── elemento.py          # Clase base para materiales # Libro, Revista, DVD
#│   ├────── utilidades.py     # Funciones auxiliares # Validaciones, etc.
#│   ├────── usuario.py         # Clases de usuarios #  Socio(Clase base),Estudiante, Profesor 
#│   ├────── biblioteca.py    # Clase principal del sistema # Gestión de materiales y usuarios
#├── app.py                      # Archivo principal para ejecutar la aplicación
#├── data/                       # Carpeta para almacenar archivos de datos
#├── gui/                    # Carpeta para la interfaz gráfica # Tkinter  Parte Martin 


