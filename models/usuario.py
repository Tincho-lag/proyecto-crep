# usuario.py

class Administrador:  # desarrollar luego
    def __init__(self, id, nombre, ):
        self.__id = id
        self.__nombre = nombre

class Usuario:
    def __init__(self, id, nombre, domicilio, material_prestado = []):
        self.id = id
        self.nombre = nombre
        self.domicilio = domicilio
        self.__material_prestado = []  #lista para rastrear materiales prestados

class Estudiante(Usuario):
    def __init__(self, id, nombre, domicilio, carrera, tipo ): 
        super().__init__(carrera)
        self.carrera = carrera
        self.tipo = "Estudiante"

class Profesor(Usuario):
    def __init__(self, id, nombre, domicilio, carrera, tipo ):
        super().__init__()
        self.tipo = "Profesor"

    # setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_telefono(self, telefono):
        self.__telefono = telefono 

    # getters
    def get_id_socio(self):
        return self.__id_socio

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_material_prestado(self):
        return self.__material_prestado

    # setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_telefono(self, telefono):
        self.__telefono = telefono




#biblioteca_sistema 

#├── models/a
#│   ├── element
#│   ├────── elemento.py          # Clase base para materiales (TU ENFOQUE INICIAL)
#│   ├────── utilidades.py           # Herencias de libros
#│   ├────── usuario.py            # resolver como hacerlo

#├── date/

#├── repositories/
#│   ├── __init__.py
#│   └── material_repository.py

#├── clases/                
#│   └── interfas.py
