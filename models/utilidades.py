# utilidades.py
from collections import deque  # Importamos deque, una estructura más eficiente que list para colas

class Cola:
    def __init__(self):
        # Creamos una cola usando deque en lugar de lista
        # __items es un atributo privado
        self.__items = deque()

    def estaVacia(self):
        """Devuelve True si la cola no tiene elementos"""
        return len(self.__items) == 0

    def encolar(self, item):
        """Agrega un elemento al final de la cola (parte derecha de deque)"""
        self.__items.append(item)

    def desencolar(self):
        """Elimina y devuelve el primer elemento de la cola (parte izquierda de deque)"""
        if self.estaVacia():
            raise IndexError("La cola está vacía")  # Control de error si se intenta desencolar estando vacía
        return self.__items.popleft()  # popleft() extrae desde el inicio (FIFO)

    def verFrente(self):
        """Devuelve el primer elemento sin eliminarlo"""
        if self.estaVacia():
            raise IndexError("La cola está vacía")
        return self.__items[0]  # Acceso directo al primer elemento

    def tamanio(self):
        """Devuelve la cantidad de elementos en la cola"""
        return len(self.__items)

    def verFinal(self):
        """Devuelve el último elemento sin eliminarlo"""
        if self.estaVacia():
            raise IndexError("La cola está vacía")
        return self.__items[-1]  # Acceso al último elemento

    def limpiar(self):
        """Vacía completamente la cola"""
        self.__items.clear()

    def contiene(self, item):
        """Verifica si un elemento está dentro de la cola"""
        return item in self.__items

    def clonar(self):
        """Crea y devuelve una nueva Cola con los mismos elementos"""
        nuevaCola = Cola()
        nuevaCola.__items = self.__items.copy()  # Copiamos los elementos
        return nuevaCola

    def invertir(self):
        """Invierte el orden de los elementos en la cola"""
        self.__items.reverse()

    def toLista(self):
        """Convierte la cola a una lista normal de Python"""
        return list(self.__items)

    def encolarFrente(self, item):
        """Agrega un elemento al frente de la cola (lado izquierdo de deque)"""
        self.__items.appendleft(item)

    from clase_pila import Pila 
texto = Pila()
while True:
    palabra = input("escriba una palabra (o 'fin' para terminar): ")
    if palabra == "fin":
        break
    texto.push(palabra)
    print("historial de ultima palabra:",texto.peek())

    deshacer = input("si desea deshacer la ultima palabra ingese (s/n):")
    if deshacer == "s" or deshacer == "S":
        texto.pop()
        if not texto.is_empty():
            print("la palabra fue eliminada exitosamente ultima palabra:",texto.peek())

     

    
