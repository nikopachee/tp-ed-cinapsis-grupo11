from collections import deque

class Grafo:
    def __init__(self, dirigido=False):
        self.grafo = {}
        self.dirigido = dirigido

    def agregar_arista(self, u, v, peso=1):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        
        self.grafo[u].append((v, peso))
        if not self.dirigido:
            self.grafo[v].append((u, peso))

    # --- RECORRIDO BFS (Breadth-First Search / Búsqueda en Anchura) ---
    def bfs(self, inicio):
        visitados = set()
        cola = deque([inicio])
        visitados.add(inicio)
        resultado = []

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo)

            for vecino, _ in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado

    # --- RECORRIDO DFS (Depth-First Search / Búsqueda en Profundidad) ---
    def dfs(self, inicio):
        visitados = set()
        resultado = []

        def _dfs_recursivo(nodo):
            visitados.add(nodo)
            resultado.append(nodo)
            for vecino, _ in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)

        _dfs_recursivo(inicio)
        return resultado