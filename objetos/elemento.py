class Recursos: 
    def __init__(self, referencia, tipo, ejemplares_totales, ejemplares_disponibles):
        self.__referencia = referencia
        self.__tipo = tipo 
        self.__ejemplares_totales = ejemplares_totales
        self.__ejemplares_disponibles = ejemplares_disponibles
    
    def __str__(self):
        return f"recurso: {self.__referencia}, tipo: {self.__tipo}, ejemplares totales: {self.__ejemplares_totales}, ejemplares disponibles: {self.__ejemplares_disponibles}"
    
    # getters 
    def get_titulo(self): # para recursos genericos, el titulo es el tipo 
        return self.__tipo  # el tipo como clave de busqueda/ordenamiento para el arbolito
    
    def get_referencia(self):
        return self.__referencia
    
    def get_tipo(self):
        return self.__tipo 
    
    def get_ejemplares_totales(self): # disponibles totales
        return self.__ejemplares_totales
    
    def get_ejemplares_disponibles(self): # disponibles para prestar
        return self.__ejemplares_disponibles
    
    # setters
    def set_ejemplares_totales(self, ejemplares):
        self.__ejemplares_totales = ejemplares

    def set_ejemplares_disponibles(self, ejemplares):
        self.__ejemplares_disponibles = ejemplares

    def set_referencia(self, referencia):
        self.__referencia = referencia
    
    # metodos (para prestar devolvver y mostrar materiales)
    def hay_disponibles(self):
        return self.__ejemplares_disponibles > 0  # devuelve true si hay ejemplares disponibles
    
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

class Libro(Recursos):
    def __init__(self, referencia, tipo, isbn, titulo, autor, ano_publicacion, ejemplares_totales, ejemplares_disponibles):
        super().__init__(referencia, tipo, ejemplares_totales, ejemplares_disponibles) 
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacion = ano_publicacion
        
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, isbn: {self.__isbn}, titulo: {self.__titulo}, autor: {self.__autor}, ano de publicacion: {self.__ano_publicacion}"
    
    # atributos especificos del libro
    def get_titulo(self):
        return self.__titulo  

    def get_isbn(self):
        return self.__isbn

    def get_autor(self):
        return self.__autor 
    
    def get_ano_publicacion(self):
        return self.__ano_publicacion