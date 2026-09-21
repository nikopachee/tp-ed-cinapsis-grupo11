class NodoArbol:
    """Cada caja del árbol: guarda UN dato y apunta a sus dos hijos."""

    def __init__(self, dato):
        self.dato = dato          # el elemento (ej: la película completa)
        self.izquierdo = None     # hijo menor (izquierda)
        self.derecho = None       # hijo mayor (derecha)


class ArbolBST:
    """Árbol Binario de Búsqueda.

    Regla de ordenamiento: en cada nodo, todo lo menor va a la izquierda
    y todo lo mayor va a la derecha. Para buscar, en cada paso descartamos
    la mitad del árbol → O(log n) promedio.
    """

    def __init__(self):
        self.raiz = None

    # Insertar
    def insertar(self, dato, clave):
        """Agrega un elemento usando `clave(dato)` para ordenar.

        clave es una función: ej. lambda p: p.titulo.lower()
        """
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato, clave)

    def _insertar_recursivo(self, nodo, dato, clave):
        if clave(dato) < clave(nodo.dato):
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.izquierdo, dato, clave)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.derecho, dato, clave)

    #  Funcion de busqueda
    def buscar(self, valor, clave):
        """Busca el elemento cuyo valor de clave == `valor`.

        Devuelve el elemento o None si no existe.
        """
        return self._buscar_recursivo(self.raiz, valor, clave)

    def _buscar_recursivo(self, nodo, valor, clave):
        if nodo is None:
            return None
        valor_nodo = clave(nodo.dato)
        if valor == valor_nodo:
            return nodo.dato
        if valor < valor_nodo:
            return self._buscar_recursivo(nodo.izquierdo, valor, clave)
        return self._buscar_recursivo(nodo.derecho, valor, clave)

    # Recorridos
    def inorder(self):
        """Izquierda → raíz → derecha. Devuelve los elementos ORDENADOS."""
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.dato)
            self._inorder_recursivo(nodo.derecho, resultado)

    def preorder(self):
        """Raíz → izquierda → derecha."""
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preorder_recursivo(nodo.izquierdo, resultado)
            self._preorder_recursivo(nodo.derecho, resultado)

    def postorder(self):
        """Izquierda → derecha → raíz."""
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierdo, resultado)
            self._postorder_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.dato)

    # Informacion
    def altura(self):
        """Profundidad máxima del árbol. Árbol vacío → 0."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_recursiva(nodo.izquierdo),
                       self._altura_recursiva(nodo.derecho))

    def esta_vacio(self):
        return self.raiz is None
