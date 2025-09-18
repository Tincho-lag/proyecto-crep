# usuario.py

class Administrador:  # desarrollar luego (no usado por ahora) se supone que puede agregar o eliminar usuarios
    def __init__(self, id, nombre, ):
        self.__id = id
        self.__nombre = nombre

class Usuario: # clase base
    def __init__(self, id, nombre, domicilio, material_prestado , estado):
        self.__id = id
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__material_prestado = []  #lista para rastrear materiales prestados
        # metodos para gestionar usuario
        self.__estado = None # por defecto activo con string "activo"

# setters usuario
    def get_id_socio(self):
        return self.__id 
    
    def get_nombre(self, nombre):
        self.__nombre = nombre  

    def get_domicilio(self, domicilio):
        self.__domicilio = domicilio

    def get_material_prestado(self, material_prestado):
        self.__material_prestado = material_prestado

    def get_estado(self, estado):
        self.__estado = estado

    def get_suspencion(self, suspencion):
        self.__suspencion = suspencion

    def get_tipo(self, tipo):
        self.__tipo = tipo          
    
class Estudiante(Usuario): # hereda de usuario puede ver libros y socilitar prestamos
    def __init__(self, id, nombre, domicilio, material_prestado, estado, suspencion, carrera, tipo ):
        super().__init__(id, nombre, domicilio, material_prestado , estado)
        self.__suspencion = suspencion
        self.__carrera = carrera
        self.__tipo = "Estudiante"
    # setters

class Profesor(Usuario): # hereda de usuario puede ver libros y solicitar prestamos
    def __init__(self, id, nombre, domicilio, material_prestado, estado, suspencion, carrera, tipo ):
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


