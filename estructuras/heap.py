import heapq

def dijkstra(grafo_obj, inicio):
    """
    Calcula la distancia mínima desde un nodo de inicio a todos los demás 
    utilizando un Min-Heap (cola de prioridad).
    """
    grafo = grafo_obj.grafo
    
    # Distancias inicializadas en infinito para todos los nodos
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    
    # Min-heap para almacenar (distancia_acumulada, nodo)
    pq = [(0, inicio)]
    
    # Para reconstruir caminos si lo necesitas
    caminos = {inicio: []}
    caminos[inicio] = [inicio]

    while pq:
        dist_actual, nodo_actual = heapq.heappop(pq)

        # Si encontramos una distancia mayor a la ya registrada, la ignoramos
        if dist_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo.get(nodo_actual, []):
            distancia = dist_actual + peso

            # Si encontramos un camino más corto al vecino
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                caminos[vecino] = caminos[nodo_actual] + [vecino]
                heapq.heappush(pq, (distancia, vecino))

    return distancias, caminos