"""
arbol_general.py — Árbol General (N-ario)

Representa una jerarquía de categorías del dominio: en este proyecto,
"Películas" como raíz, los géneros como nivel intermedio, y cada
película como hoja dentro de su género.

Uso:
    from estructuras.arbol_general import ArbolGeneral

    arbol = ArbolGeneral()
    arbol.insertar_raiz("Películas")
    nodo_genero = arbol.agregar_hijo(arbol.raiz, "Drama")
    arbol.agregar_hijo(nodo_genero, "Whiplash", dato=pelicula_whiplash)
"""


class NodoGeneral:
    """Cada nodo guarda un nombre (la categoría o el título), un dato
    opcional (solo las hojas de película lo usan) y una lista de hijos,
    que puede tener cualquier cantidad de elementos (0, 1, 2, 10...)."""

    def __init__(self, nombre, dato=None):
        self.nombre = nombre
        self.dato = dato      # None para nodos de categoría, la Pelicula para las hojas
        self.hijos = []


class ArbolGeneral:
    """Árbol N-ario: cada nodo puede tener cualquier cantidad de hijos,
    a diferencia de un árbol binario donde como máximo tiene dos."""

    def __init__(self):
        self.raiz = None

    # ==================== INSERCIÓN ====================

    def insertar_raiz(self, nombre):
        """Crea el nodo raíz del árbol."""
        self.raiz = NodoGeneral(nombre)
        return self.raiz

    def agregar_hijo(self, nodo_padre, nombre, dato=None):
        """Agrega un nuevo nodo como hijo de `nodo_padre` y lo devuelve,
        para poder encadenar más hijos debajo de él si hace falta."""
        nuevo_nodo = NodoGeneral(nombre, dato)
        nodo_padre.hijos.append(nuevo_nodo)
        return nuevo_nodo

    # ==================== BÚSQUEDA ====================

    def buscar(self, nombre):
        """Busca un nodo por nombre (categoría o título) en todo el árbol.

        Devuelve el nodo o None si no existe. Recorre todo el árbol porque,
        a diferencia de un BST/AVL, acá no hay un orden que permita descartar
        ramas: en el peor caso hay que revisar todos los nodos → O(n).
        """
        if self.raiz is None:
            return None
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if nodo.nombre.lower() == nombre.lower():
            return nodo
        for hijo in nodo.hijos:
            encontrado = self._buscar_recursivo(hijo, nombre)
            if encontrado is not None:
                return encontrado
        return None

    # ==================== RECORRIDOS ====================

    def amplitud(self):
        """Recorrido por amplitud (BFS): nivel por nivel, de arriba hacia
        abajo y de izquierda a derecha. Usa una cola (lista como FIFO)."""
        if self.raiz is None:
            return []

        resultado = []
        cola = [self.raiz]
        while cola:
            nodo_actual = cola.pop(0)
            resultado.append(nodo_actual.nombre)
            for hijo in nodo_actual.hijos:
                cola.append(hijo)
        return resultado

    def profundidad_preorder(self):
        """Recorrido en profundidad (DFS), preorder: primero el nodo,
        después cada uno de sus hijos de izquierda a derecha."""
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.nombre)
            for hijo in nodo.hijos:
                self._preorder_recursivo(hijo, resultado)

    def profundidad_postorder(self):
        """Recorrido en profundidad (DFS), postorder: primero todos los
        hijos (recursivamente), y al final el propio nodo."""
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            for hijo in nodo.hijos:
                self._postorder_recursivo(hijo, resultado)
            resultado.append(nodo.nombre)

    # ==================== INFORMACIÓN ====================

    def obtener_niveles(self):
        """Devuelve un diccionario {nivel: [nombres]} agrupando los nodos
        por profundidad (la raíz está en el nivel 0)."""
        niveles = {}
        if self.raiz is None:
            return niveles

        cola = [(self.raiz, 0)]
        while cola:
            nodo_actual, nivel = cola.pop(0)
            niveles.setdefault(nivel, []).append(nodo_actual.nombre)
            for hijo in nodo_actual.hijos:
                cola.append((hijo, nivel + 1))
        return niveles

    def altura(self):
        """Profundidad máxima del árbol. Árbol vacío → 0."""
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self._altura_recursiva(hijo) for hijo in nodo.hijos)

    def cantidad_nodos(self):
        """Cuenta todos los nodos del árbol (categorías + hojas)."""
        return self._contar_recursivo(self.raiz)

    def _contar_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + sum(self._contar_recursivo(hijo) for hijo in nodo.hijos)
