# elemento.py 
# posible inicio para las herencias del libro 
class Elemento:
    def __init__(self, isbn, titulo, autor, ejemplares =1):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__ejemplares_disponibles = ejemplares  # Estado de disponibilidad Boleano
# getters 
    def get_isbn(self):
        return self.__isbn
    
    def get_titulo(self):
        return self.__titulo   
         
    def get_autor(self):
        return self.__autor 
    
    def get_ejemplares_disponibles(self): # getters para disponibilidad
        return self.__ejemplares_disponibles
 
# setters (modificar disponibilidad)
    def set_ejemplares_disponibles(self, ejemplares):
        self.__ejemplares_disponibles = ejemplares 

# metodos para prestar y devolver
    def prestar(self):
        if self.__ejemplares_disponibles > 0:
            self.__ejemplares_disponibles -= 1
            return True
        return False   

    def devolver(self):
        self.__ejemplares_disponibles += 1

# clase libro que hereda de elemento
class Libro(Elemento):
    def __init__(self, isbn, titulo, autor, año_publicacion,ejemplares =1 ):
        super().__init__(isbn, titulo, autor, ejemplares)
        self.__año_publicacion = año_publicacion

    def get_año_publicacion(self):
        return self.__año_publicacion
    
 # representacion del objeto
    
    def __str__(self):
                return f"{self.get_titulo()} por {self.get_autor()}, ISBN: {self.get_isbn()}, Año: {self.get_año_publicacion()}, Disponibles: {self.get_ejemplares_disponibles()}"

        # Usamos los getters para acceder a los atributos de la clase base

