class NodoArbol:
    def __init__(self, material):
        self.material = material
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, material):
        if self.raiz is None:
            self.raiz = NodoArbol(material)
        else:
            self._insertar_recursivo(self.raiz, material)
    
    def _insertar_recursivo(self, nodo, material):
        # ordenar alfabaticamente por titulo
        titulo_nuevo = material.get_titulo().lower()
        titulo_nodo = nodo.material.get_titulo().lower()
        if titulo_nuevo < titulo_nodo:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(material)
            else:
                self._insertar_recursivo(nodo.izquierdo, material)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(material)
            else:
                self._insertar_recursivo(nodo.derecho, material)
    
    def buscar_por_titulo(self, titulo):
        return self._buscar_recursivo(self.raiz, titulo)
    
    def _buscar_recursivo(self, nodo, titulo):
        if nodo is None:
            return None
        titulo_lower = titulo.lower()
        titulo_nodo = nodo.material.get_titulo().lower()
        if titulo_lower == titulo_nodo:
            return nodo.material
        elif titulo_lower < titulo_nodo:
            return self._buscar_recursivo(nodo.izquierdo, titulo)
        else:
            return self._buscar_recursivo(nodo.derecho, titulo)
    
    def listar_todos(self):
        materiales = []
        self._inorden(self.raiz, materiales)
        return materiales
    
    def _inorden(self, nodo, materiales):
        if nodo is not None:
            self._inorden(nodo.izquierdo, materiales)
            materiales.append(nodo.material)
            self._inorden(nodo.derecho, materiales)