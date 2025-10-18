from datetime import date, timedelta

class Administrador:  
    # hacer despues (no usado por ahora) se supone que  
    # solo esta clase puede agregar o eliminar usuarios 
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

class Usuario: 
    def __init__(self, id, nombre, domicilio):
        self.__id = id
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__material_prestado = []  # lista para rastrear materiales prestados
        self.__estado = "activo" # puede ser activo o suspendido
        self.__fecha_fin_suspension = None

    # setters usuario modificar datos
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio
        
    # getters usuario
    def get_id(self):
        return self.__id 
    
    def get_nombre(self):
        return self.__nombre
 
    def get_domicilio(self):
        return self.__domicilio

    def get_material_prestado(self):
        return self.__material_prestado

    def get_estado(self):
        return self.__estado  

    # metodos para gestionar prestamos
    def prestar_material(self, isbn):
        self.__material_prestado.append(isbn)
    
    def devolver_material(self, isbn):
        if isbn in self.__material_prestado:
            self.__material_prestado.remove(isbn)
    
    def estado_activo(self):
        if self.__estado == "activo":
            return True
        if self.__estado == "suspendido" and self.__fecha_fin_suspension:
            try:
                if date.today() >= self.__fecha_fin_suspension:
                    self.reactivar()
                    return True
            except Exception:
                pass
        return self.__estado == "activo"
    
    def suspender(self, dias):
        self.__estado = "suspendido" 
        if dias and dias > 0:
            self.__fecha_fin_suspension = date.today() + timedelta(days=dias)
        else:
            self.__fecha_fin_suspension = None  # suspension indefinida

    def reactivar(self):
        self.__estado = "activo"
        self.__fecha_fin_suspension = None

    def __str__(self):
        estado_texto = "activo" if self.estado_activo() else "suspendido"
        return f"{self.get_nombre()} (id: {self.get_id()}) - {estado_texto}"

class Estudiante(Usuario): # hereda de usuario puede ver libros y solicitar prestamos
    def __init__(self, id, nombre, domicilio):
        super().__init__(id, nombre, domicilio)
        self.__tipo = "estudiante" 

    # tres articulos dos dias de prestamo para estudiantes 
    def get_limite_prestamos(self):
        return 3

    def get_dias_prestamo(self):
        return 2

class Profesor(Usuario): # hereda de usuario puede ver libros y solicitar prestamos
    def __init__(self, id, nombre, domicilio):
        super().__init__(id, nombre, domicilio)
        self.__tipo = "profesor" 

    # cinco articulos y 7 dias de prestamo para profesores 
    def get_limite_prestamos(self):
        return 5

    def get_dias_prestamo(self):
        return 5