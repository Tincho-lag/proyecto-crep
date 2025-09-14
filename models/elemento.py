# elemento.py 
# posible inicio para las herencias del libro 
class Elemento:
    def __init__(self, isbn, titulo, autor, ejemplares =1):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__ejemplares_disponible = ejemplares  # Estado de disponibilidad Boleano
# getters 
    def get_isbn(self):
        return self.__isbn
    def get_titulo(self):
        return self.__titulo        
    def get_autor(self):
        return self.__autor 
    def get_ejemplares_disponibles(self): # getters para disponibilidad
        return self.__ejemplares_disponibles
    def get_todos_los_elementos(self):
       return self._todos_los_elementos
 
# setters (modificar disponibilidad)
    def set_ejemplares_disponible(self, ejemplares):
        self.__ejemplares_disponible = ejemplares 

# metodos para prestar y devolver
    def prestar(self):
        if self.__ejemplares_disponible:
            self.__ejemplares_disponible = False
            return True
        return False   

    def devolver(self):
        self.__disponible = True

# clase libro que hereda de elemento
class Libro(Elemento):
    def __init__(self, isbn, titulo, autor, año_publicacion,ejemplares =1 ):
        super().__init__(isbn, titulo, autor, ejemplares =1 )
        self._año_publicacion = año_publicacion

    def año_publicacion(self):
        return self.año_publicacion
    
 # Sobreescribe representación
    def __str__(self):
        return f"Libro: {self.get_titulo()} por {self.get_autor()} (ISBN: {self.get_isbn()}, Año: {self._año_publicacion}, Disponibles: {self.get_ejemplares_disponibles()})"
