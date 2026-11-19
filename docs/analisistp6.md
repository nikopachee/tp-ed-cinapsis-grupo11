## Análisis TP6 - Heap (MaxHeap)
## .1 ¿Qué resolvió?
Necesitábamos mostrar las películas mejor calificadas del catálogo sin tener que ordenar todas las películas cada vez que el usuario solicitara un ranking.

Para resolver este problema implementamos un MaxHeap, donde cada película se almacena utilizando como prioridad su rating y, en caso de empate, el año de estreno.

La opción "Pedir ranking de mejores películas" utiliza esta estructura para obtener rápidamente los títulos mejor valorados.

## .2 ¿Por qué un Heap?
Una lista común requiere ordenar todos los elementos cada vez que se necesita conocer cuáles son las películas con mejor puntuación.

El MaxHeap mantiene automáticamente el elemento de mayor prioridad en la raíz, permitiendo acceder rápidamente a él sin recorrer toda la colección.

Además, las inserciones mantienen la propiedad del heap mediante reordenamientos locales, evitando ordenamientos completos.

### .3 Prueba del Heap
Salida de ejemplo:

¿Cuántas películas querés ver en el ranking?: 5

--- TOP 5 MEJORES CALIFICADAS ---

El Padrino (1972) - ★ 9.2
Matrix (1999) - ★ 9.0
Inception (2010) - ★ 8.8
Interstellar (2014) - ★ 8.6
Parásitos (2019) - ★ 8.6

### 4 Complejidad
Obtener el máximo: O(1)
Insertar: O(log n)
Extraer máximo: O(log n)
Construcción del heap: O(n log n)
El elemento con mayor prioridad siempre permanece accesible en la raíz.

### .5 Conclusión
El MaxHeap resultó la estructura más adecuada para implementar rankings de películas.

Permite acceder rápidamente a las películas mejor calificadas y evita ordenar constantemente toda la colección de datos.