from collections import deque


class Grafo:
    def __init__(self, dirigido=False, clave=lambda x: x):
        self.dirigido = dirigido
        self.clave = clave
        # {id_nodo: {"dato": elemento, "vecinos": {id_vecino: peso}}}
        self.adyacencia = {}

    def agregar_vertice(self, elemento):
        id_nodo = self.clave(elemento)
        if id_nodo not in self.adyacencia:
            self.adyacencia[id_nodo] = {"dato": elemento, "vecinos": {}}

    def agregar_arista(self, origen, destino, peso=1):
        id_origen = self.clave(origen)
        id_destino = self.clave(destino)

        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

        if id_origen != id_destino:
            self.adyacencia[id_origen]["vecinos"][id_destino] = peso
            if not self.dirigido:
                self.adyacencia[id_destino]["vecinos"][id_origen] = peso

    def bfs(self, id_origen, max_saltos=None):
        """Recorrido en anchura. Retorna lista de tuplas (dato, nivel)."""
        if id_origen not in self.adyacencia:
            return []

        visitados = {id_origen}
        cola = deque([(id_origen, 0)])
        resultado = []

        while cola:
            actual, nivel = cola.popleft()
            if nivel > 0:
                resultado.append((self.adyacencia[actual]["dato"], nivel))

            if max_saltos is None or nivel < max_saltos:
                for vecino in self.adyacencia[actual]["vecinos"]:
                    if vecino not in visitados:
                        visitados.add(vecino)
                        cola.append((vecino, nivel + 1))

        return resultado

    def dfs(self, id_origen):
        """Recorrido en profundidad. Retorna lista con los datos visitados."""
        if id_origen not in self.adyacencia:
            return []

        visitados = set()
        recorrido = []

        def _dfs(nodo):
            visitados.add(nodo)
            recorrido.append(self.adyacencia[nodo]["dato"])
            for vecino in self.adyacencia[nodo]["vecinos"]:
                if vecino not in visitados:
                    _dfs(vecino)

        _dfs(id_origen)
        return recorrido

    def camino_minimo(self, id_origen, id_destino):
        """Algoritmo de Dijkstra. Retorna (lista_de_datos, costo_total)."""
        if id_origen not in self.adyacencia or id_destino not in self.adyacencia:
            return None, float("inf")

        distancias = {nodo: float("inf") for nodo in self.adyacencia}
        predecesores = {nodo: None for nodo in self.adyacencia}
        distancias[id_origen] = 0
        no_visitados = set(self.adyacencia.keys())

        while no_visitados:
            actual = min(no_visitados, key=lambda n: distancias[n])
            if distancias[actual] == float("inf") or actual == id_destino:
                break
            no_visitados.remove(actual)

            for vecino, peso in self.adyacencia[actual]["vecinos"].items():
                if vecino in no_visitados:
                    nueva_dist = distancias[actual] + peso
                    if nueva_dist < distancias[vecino]:
                        distancias[vecino] = nueva_dist
                        predecesores[vecino] = actual

        if distancias[id_destino] == float("inf"):
            return None, float("inf")

        camino = []
        paso = id_destino
        while paso is not None:
            camino.append(self.adyacencia[paso]["dato"])
            paso = predecesores[paso]
        camino.reverse()

        return camino, distancias[id_destino]