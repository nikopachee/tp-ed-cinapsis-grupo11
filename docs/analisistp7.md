### análisis TP7 - Grafos
## 1 ¿Qué resolvió?
Necesitábamos representar relaciones entre películas para poder generar recomendaciones y recorridos temáticos.

Una película puede estar relacionada con varias otras simultáneamente, por lo que una estructura jerárquica como un árbol no resulta adecuada para modelar estas conexiones.

Para resolver este problema implementamos un grafo no dirigido.

## 2 ¿Por qué un Grafo?
Cada película se representa como un vértice.

Las relaciones entre películas se representan mediante aristas con distintos niveles de afinidad:

Peso 1: mismo género y misma década.
Peso 2: mismo género.
Peso 3: misma década.
Ejemplo:

Matrix | Interstellar | Inception

El grafo permite modelar múltiples conexiones entre elementos y constituye la base para BFS, DFS y Dijkstra.

## 3 Representación utilizada
Se seleccionó una lista de adyacencia.

self.adyacencia = {}
{
    "dato": pelicula,
    "vecinos": {
        vecino: peso
    }
}

## 4 Complejidad
Agregar vértice: O(1)
Agregar arista: O(1)
Obtener vecinos: O(grado del vértice)

La eficiencia obtenida resulta adecuada para la cantidad de películas manejadas por el sistema.

## 5 Conclusión

El grafo permitió representar afinidades entre películas de forma flexible.

Además, se convirtió en la estructura fundamental para implementar recomendaciones, maratones temáticas y caminos mínimos en las siguientes etapas.