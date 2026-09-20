class NodoArbol:
    def __init__(self, dato):
        """Cada caja del arbol. Tiene un dato y hasta dos hijos."""
        self.dato = dato        # El elemento (ej: la película)
        self.izquierda = None   # Hijo menor (va hacia la izquierda)
        self.derecha = None     # Hijo mayor (va hacia la derecha)


class ArbolBST:
    """Árbol Binario de Búsqueda ordenado por clave del elemento."""

    def __init__(self):
        self.raiz = None

    # ---------- INSERTAR ----------
    def insertar(self, dato, clave):
        """Agrega un elemento. `clave` es una función que devuelve el valor
        por el que se ordena (ej: lambda p: p.titulo.lower())."""
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato, clave)

    def _insertar_recursivo(self, nodo, dato, clave):
        if clave(dato) < clave(nodo.dato):
            if nodo.izquierda is None:  # Corregido: 'izquierda' en lugar de 'izquierdo'
                nodo.izquierda = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.izquierda, dato, clave)
        else:
            if nodo.derecha is None:    # Corregido: 'derecha'
                nodo.derecha = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.derecha, dato, clave)

    # ---------- BUSCAR ----------
    def buscar(self, valor, clave):
        """Busca por valor. Devuelve el dato del elemento o None si no existe."""
        return self._buscar_recursivo(self.raiz, valor, clave)

    def _buscar_recursivo(self, nodo, valor, clave):
        if nodo is None:
            return None
        
        # Comparación corregida: se compara el string buscado con clave(nodo.dato)
        if clave(nodo.dato) == valor:
            return nodo.dato  # Devuelve el objeto guardado (la película), no la caja NodoArbol
            
        if valor < clave(nodo.dato):
            return self._buscar_recursivo(nodo.izquierda, valor, clave)
        else:
            return self._buscar_recursivo(nodo.derecha, valor, clave)

    # ---------- RECORRIDOS ----------
    def inorder(self):
        """Izquierda → raíz → derecha. Devuelve los elementos ORDENADOS."""
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self._inorder_recursivo(nodo.derecha, resultado)

    def preorder(self):
        """Raíz → izquierda → derecha."""
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self._preorder_recursivo(nodo.izquierda, resultado)
            self._preorder_recursivo(nodo.derecha, resultado)

    def postorder(self):
        """Izquierda → derecha → raíz."""
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorder_recursivo(nodo.izquierda, resultado)
            self._postorder_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.dato)

    # ---------- EXTRA: mostrar la estructura ----------
    def altura(self):
        """Profundidad máxima del árbol."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        # Corregidos nombres de atributos y operador duplicado '++'
        return 1 + max(self._altura_recursiva(nodo.izquierda),
                       self._altura_recursiva(nodo.derecha))