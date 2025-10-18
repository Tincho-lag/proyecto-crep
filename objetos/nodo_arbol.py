# objetos/nodo_arbol.py

class NodoArbol:
    """nodo del arbol binario que contiene un material"""
    def __init__(self, material):
        self.material = material
        self.izquierdo = None  # hijo izquierdo (menor alfabeticamente)
        self.derecho = None    # hijo derecho (mayor alfabeticamente)


class ArbolBinario:
    """arbol binario de busqueda para ordenar materiales alfabeticamente"""
    def __init__(self):
        self.raiz = None  # el arbol comienza vacio
    
    def insertar(self, material):
        """inserta un material en el arbol manteniendo orden alfabetico"""
        if self.raiz is None:
            # primer material: se convierte en la raiz
            self.raiz = NodoArbol(material)
        else:
            # ya hay materiales: buscar posicion correcta recursivamente
            self._insertar_recursivo(self.raiz, material)
    
    def _insertar_recursivo(self, nodo, material):
        # metodo recursivo privado para insertar en posicion correcta
        # comparar titulos en minusculas para ordenamiento correcto
        titulo_nuevo = material.get_titulo().lower()
        titulo_nodo = nodo.material.get_titulo().lower()
        
        if titulo_nuevo < titulo_nodo:
            # va a la izquierda (menor alfabeticamente)
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(material)
            else:
                self._insertar_recursivo(nodo.izquierdo, material)
        else:
            # va a la derecha (mayor o igual alfabeticamente)
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(material)
            else:
                self._insertar_recursivo(nodo.derecho, material)
    
    def buscar_por_titulo(self, titulo):
        """busca un material por titulo de forma eficiente O(log n)"""
        return self._buscar_recursivo(self.raiz, titulo)
    
    def _buscar_recursivo(self, nodo, titulo):
        """metodo recursivo privado para buscar"""
        if nodo is None:
            # no encontrado
            return None
        
        # comparar en minusculas para busqueda case-insensitive
        titulo_lower = titulo.lower()
        titulo_nodo = nodo.material.get_titulo().lower()
        
        if titulo_lower == titulo_nodo:
            # encontrado
            return nodo.material
        elif titulo_lower < titulo_nodo:
            # buscar en subarbol izquierdo
            return self._buscar_recursivo(nodo.izquierdo, titulo)
        else:
            # buscar en subarbol derecho
            return self._buscar_recursivo(nodo.derecho, titulo)
    
    def listar_todos(self):
        # devuelve lista ordenada alfabeticamente de todos los materiales
        materiales = []
        self._inorden(self.raiz, materiales)
        return materiales
    
    def _inorden(self, nodo, materiales):
        # recorrido inorden (izquierda-raiz-derecha) da orden alfabetico
        if nodo is not None:
            self._inorden(nodo.izquierdo, materiales)
            materiales.append(nodo.material)
            self._inorden(nodo.derecho, materiales)
