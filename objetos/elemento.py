# objetos/elemento.py

class Recursos: 
    # clase base para todos los materiales de la biblioteca
    def __init__(self, referencia, tipo, ejemplares_totales, ejemplares_disponibles):
        # atributos privados (encapsulamiento)
        self.__referencia = referencia
        self.__tipo = tipo 
        self.__ejemplares_totales = ejemplares_totales
        self.__ejemplares_disponibles = ejemplares_disponibles
    
    def __str__(self):
        # metodo para mostrar la salida
        return f"recurso: {self.__referencia}, tipo: {self.__tipo}, ejemplares totales: {self.__ejemplares_totales}, ejemplares disponibles: {self.__ejemplares_disponibles}"
    
    # getters - metodos para obtener valores privados
    def get_titulo(self):
        # para recursos genericos, el titulo es el tipo (ej: "cargador")
        # esto permite que el arbol binario ordene por tipo
        return self.__tipo
    
    def get_referencia(self):
        return self.__referencia
    
    def get_tipo(self):
        return self.__tipo 
    
    def get_ejemplares_totales(self):
        return self.__ejemplares_totales
    
    def get_ejemplares_disponibles(self):
        return self.__ejemplares_disponibles
    
    # metodos de negocio - logica de prestamo/devolucion
    def hay_disponibles(self):
        # verifica si quedan ejemplares para prestar
        return self.__ejemplares_disponibles > 0
    
    def prestar(self):
        # reduce en 1 los ejemplares disponibles si hay stock
        if self.__ejemplares_disponibles > 0:
            self.__ejemplares_disponibles -= 1
            return True
        return False

    def devolver(self):
        # aumenta en 1 los disponibles sin exceder el total
        if self.__ejemplares_disponibles < self.__ejemplares_totales:
            self.__ejemplares_disponibles += 1
            return True
        return False


class Libro(Recursos):
    """clase libro hereda de recursos (tiene atributos adicionales)"""
    def __init__(self, referencia, tipo, isbn, titulo, autor, ano_publicacion, ejemplares_totales, ejemplares_disponibles):
        # llama al constructor de la clase padre
        super().__init__(referencia, tipo, ejemplares_totales, ejemplares_disponibles) 
        # atributos especificos de libro
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacion = ano_publicacion
        
    def __str__(self):
        # sobreescribe el metodo de la clase padre agregando info del libro
        base_str = super().__str__()
        return f"{base_str}, isbn: {self.__isbn}, titulo: {self.__titulo}, autor: {self.__autor}, ano: {self.__ano_publicacion}"
    
    # getters especificos de libro
    def get_titulo(self):
        # sobreescribe get_titulo() para devolver el titulo real del libro
        return self.__titulo

    def get_isbn(self):
        return self.__isbn

    def get_autor(self):
        return self.__autor 
    
    def get_ano_publicacion(self):
        return self.__ano_publicacion

