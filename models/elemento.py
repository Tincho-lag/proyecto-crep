# elemento.py 
## clase base para materiales 
class Recursos: # clase base
    def __init__(self, referencia, tipo, ejemplares ):
        # atributos basicos
        self.__referencia = referencia
        self.__tipo = tipo
        # metodos para gestionar ejemplares
        self.__ejemplares_totales = ejemplares 
        self.__ejemplares_disponibles = ejemplares  

# getters genericos
    def get_referencia(self):
        return self.__referencia
    
    def get_tipo(self):
        return self.__tipo
    
    def get_ejemplares_totales(self): # disponibles totales
        return self.__ejemplares_totales
    
    def get_ejemplares_disponibles(self): # disponibles para prestar
        return self.__ejemplares_disponibles

## clase libro que hereda de recursos
class Libro(Recursos):
    def __init__(self, referencia, tipo, ejemplares, isbn, titulo, autor, año_publicacion ):
        super().__init__(referencia, tipo, ejemplares)
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
  
    # atributos especificos del libro
    def get_isbn(self):
        return self.__isbn
    
    def get_año_publicacion(self):
        return self.__año_publicacion

    def get_titulo(self):
        return self.__titulo   
         
    def get_autor(self):
        return self.__autor 
    
    # metodos libro (para prestar devolvver y mostrar libros)
    def prestar(self):
        if self.__ejemplares_disponibles > 0:
                self.__ejemplares_disponibles -= 1
                return True
        else:
                return False
        
    def mostrar_disponibles(self):
        return self.__ejemplares_disponibles
    
    def devolver(self):
        if self.__ejemplares_disponibles < self.__ejemplares_totales:
             self.__ejemplares_disponibles += 1
        else:
             return False
