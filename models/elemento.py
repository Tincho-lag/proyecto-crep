# elemento.py 
# posible inicio para las herencias del libro 
class Elemento: # clase base
    def __init__(self, referencia, tipo, ejemplares):
        self.__referencia = referencia
        self.__tipo = tipo
        self.__ejemplares = ejemplares 

# clase libro que hereda de elemento
class Libro(Elemento):
    def __init__(self, referencia, tipo, ejemplares, isbn, titulo, autor, año_publicacion ):
        super().__init__(tipo, ejemplares)
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion

    def get_isbn(self):
        return self.__isbn
    
    def get_año_publicacion(self):
        return self.__año_publicacion

    def get_titulo(self):
        return self.__titulo   
         
    def get_autor(self):
        return self.__autor 

# setters (modificar disponibilidad)
    def set_ejemplares(self, ejemplares):
        self.__ejemplares = ejemplares

# metodos para prestar y devolver
    def prestar(self):
        if self.__ejemplares_disponibles > 0:
            self.__ejemplares_disponibles -= 1
            return True
        return False   

    def devolver(self):
        self.__ejemplares_disponibles += 1

 # representacion del objeto
    
    def __str__(self):
                return f"{self.get_titulo()} por {self.get_autor()}, ISBN: {self.get_isbn()}, Año: {self.get_año_publicacion()}, Disponibles: {self.get_ejemplares_disponibles()}"

        # Usamos los getters para acceder a los atributos de la clase base

