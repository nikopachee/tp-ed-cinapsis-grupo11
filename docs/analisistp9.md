### Análisis TP9 - Camino Mínimo (Dijkstra)
# 1 ¿Qué resolvió?
Necesitábamos permitir que el usuario descubriera una secuencia lógica de películas entre dos títulos del catálogo.

Para ello implementamos el algoritmo de Dijkstra utilizando el grafo de similitud construido en etapas anteriores.

La funcionalidad se encuentra disponible mediante la opción:

"Maratón óptima entre películas".

# 2 ¿Por qué Dijkstra?
Las relaciones del grafo poseen distintos niveles de afinidad.

Cada arista recibe un peso según la similitud entre películas:

Peso 1: mismo género y misma década.
Peso 2: mismo género.
Peso 3: misma década.
Las conexiones con menor peso representan relaciones más fuertes.

Debido a que las conexiones poseen costos diferentes, BFS y DFS no permiten encontrar la mejor ruta posible.

Dijkstra fue seleccionado porque calcula el camino de menor costo acumulado entre dos nodos.

# 3 Aplicación dentro del sistema
El usuario selecciona una película de origen y una película de destino.

A partir de esos dos puntos, el sistema analiza todas las conexiones disponibles y encuentra la secuencia de películas con mayor afinidad posible.

Ejemplo:
==================================================
🎬 MARATÓN ÓPTIMA ENTRE PELÍCULAS
==================================================

Origen: Matrix
Destino: Interstellar

Películas conectadas: 2
Afinidad total del recorrido: 2

Recorrido recomendado:

1. Matrix (Ciencia ficción, 1999) ★ 9.0
2. Interstellar (Ciencia ficción, 2014) ★ 8.6

--------------------------------------------------


La afinidad total representa la suma de los pesos utilizados durante el recorrido.

Cuanto menor sea el valor obtenido, más relacionadas se encuentran las películas seleccionadas.

# 4 Complejidad
La implementación utiliza una colección de vértices no visitados.

Complejidad temporal:

O(V²)

donde:

V representa la cantidad de vértices del grafo.
Para conjuntos de datos más grandes podría optimizarse utilizando una cola de prioridad.

# 5 Diferencias con BFS y DFS
BFS:

Busca recomendaciones cercanas.
Prioriza los vecinos inmediatos.
DFS:

Explora una rama completa del grafo.
Permite construir maratones temáticas.
Dijkstra:

Considera los pesos de las conexiones.
Busca el camino de menor costo posible entre dos películas.

# 6 Conclusión
La incorporación de Dijkstra permitió transformar el grafo de similitudes en una herramienta de navegación inteligente.

A diferencia de BFS y DFS, el algoritmo tiene en cuenta la intensidad de las relaciones entre películas y construye recorridos optimizados, ofreciendo al usuario una transición progresiva entre dos títulos del catálogo.