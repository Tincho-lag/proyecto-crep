# objetos/usuario.py

from datetime import date, timedelta

class Usuario: 
    # clase base para usuarios de la biblioteca
    def __init__(self, id, nombre, domicilio):
        self.__id = id
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__material_prestado = []  # lista de titulos prestados
        self.__estado = "activo"
        self.__fecha_fin_suspension = None

    # getters
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

    # metodos de gestion de prestamos
    def prestar_material(self, titulo):
        # registra que el usuario tomo prestado un material
        self.__material_prestado.append(titulo)
    
    def devolver_material(self, titulo):
        # registra que el usuario devolvio un material
        if titulo in self.__material_prestado:
            self.__material_prestado.remove(titulo)
    
    def estado_activo(self):
        # verifica si el usuario puede hacer prestamos
        # si esta suspendido, verificar si ya paso la fecha de suspension
        if self.__estado == "suspendido" and self.__fecha_fin_suspension:
            if date.today() >= self.__fecha_fin_suspension:
                # suspension termino: reactivar automaticamente
                self.reactivar()
                return True
        return self.__estado == "activo"
    
    def suspender(self, dias):
        # suspende al usuario por X dias
        self.__estado = "suspendido"
        if dias and dias > 0:
            self.__fecha_fin_suspension = date.today() + timedelta(days=dias)

    def reactivar(self):
        # reactiva un usuario suspendido
        self.__estado = "activo"
        self.__fecha_fin_suspension = None

    def __str__(self):
        estado_texto = "activo" if self.estado_activo() else "suspendido"
        return f"{self.get_nombre()} (id: {self.get_id()}) - {estado_texto}"


class Estudiante(Usuario):
    # estudiante: limite 3 materiales, 2 dias de prestamo
    def __init__(self, id, nombre, domicilio):
        super().__init__(id, nombre, domicilio)
        self.__tipo = "estudiante"

    def get_limite_prestamos(self):
        return 3

    def get_dias_prestamo(self):
        return 2


class Profesor(Usuario):
    # profesor: limite 5 materiales, 5 dias de prestamo
    def __init__(self, id, nombre, domicilio):
        super().__init__(id, nombre, domicilio)
        self.__tipo = "profesor"

    def get_limite_prestamos(self):
        return 5

    def get_dias_prestamo(self):
        return 5