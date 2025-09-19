# objetos/elemento.py 

class Recursos: # clase base
    def __init__(self, referencia, tipo, ejemplares ):
        self.__referencia = referencia
        self.__tipo = tipo 
        self.__ejemplares_totales = ejemplares 
        self.__ejemplares_disponibles = ejemplares  

# getters 
    def get_referencia(self):
        return self.__referencia
    
    def get_tipo(self):
        return self.__tipo
    
    def get_ejemplares_totales(self): # disponibles totales
        return self.__ejemplares_totales
    
    def get_ejemplares_disponibles(self): # disponibles para prestar
        return self.__ejemplares_disponibles
    
# setters
    def set_referencia(self, referencia):
        self.__referencia = referencia
    
# metodos (para prestar devolvver y mostrar materiales)
    def hay_disponibles(self):
        return self.__ejemplares_disponibles > 0  # devuelve True si hay ejemplares disponibles
    
    def prestar(self):
        if self.__ejemplares_disponibles > 0:
                self.__ejemplares_disponibles -= 1 # si hay mas de 0 ejemplares disponibles reduce de a 1
                return True
        else:
                return False

    def devolver(self):
        if self.__ejemplares_disponibles < self.__ejemplares_totales: # si hay menos ejemplares disponibles que el total
             self.__ejemplares_disponibles += 1 # aumenta en 1
             return True
        else:
             return False

def __str__(self):
        return f"{self.__tipo} {self.__referencia} - Disponibles: {self.__ejemplares_disponibles}/{self.__ejemplares_totales}"


class Libro(Recursos):
    def __init__(self, referencia, tipo, isbn, titulo, autor, año_publicacion,ejemplares ):
        super().__init__(referencia, tipo, ejemplares) 
        self.__tipo = "Libro"
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
  

    # atributos especificos del libro
    
    def get_isbn(self):
        return self.__isbn
    
    def get_titulo(self):
        return self.__titulo  
    
    def get_autor(self):
        return self.__autor 
    
    def get_año_publicacion(self):
        return self.__año_publicacion 
         

def __str__(self):
    return f"{self.get_titulo()} por {self.get_autor()}, ISBN: {self.get_isbn()}, Disponibles: {self.get_ejemplares_disponibles()}/{self.get_ejemplares_totales()}"
