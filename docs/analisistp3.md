# Análisis TP3 — Árbol Binario de Búsqueda
1. ¿Qué resolvimos?

Incorporamos un árbol binario de búsqueda (BST) para resolver la búsqueda por título de forma más eficiente. La opción "Buscar" del menú ahora usa el árbol en vez de recorrer la lista.

2. Clave de ordenamiento

Ordenamos por título (p.titulo.lower()) porque es el campo por el que el usuario busca en el menú de la terminal, así la búsqueda queda directa sin tener que recorrer atributos adicionales.

3. Prueba del árbol

Salida de python algoritmos/probar_bst.py:

Altura del árbol: 5

--- inorder (ordenado alfabéticamente) ---
  Coco (2017) - Animación - Rating: 8.4 - Estado: Pendiente
  El Origen del Planeta de los Simios (2011) - Ciencia ficción - Rating: 7.6 - Estado: Pendiente
  El Padrino (1972) - Drama - Rating: 9.2 - Estado: Pendiente
  Inception (2010) - Ciencia ficción - Rating: 8.8 - Estado: Pendiente
  Interstellar (2014) - Ciencia ficción - Rating: 8.6 - Estado: Pendiente
  Joker (2019) - Drama - Rating: 8.4 - Estado: Pendiente
  La La Land (2016) - Musical - Rating: 8.0 - Estado: Pendiente
  Matrix (1999) - Ciencia ficción - Rating: 9.0 - Estado: Pendiente
  Parásitos (2019) - Drama - Rating: 8.6 - Estado: Pendiente
  Titanic (1997) - Romance - Rating: 7.8 - Estado: Pendiente
  Toy Story (1995) - Animación - Rating: 8.3 - Estado: Pendiente
  Whiplash (2014) - Drama - Rating: 8.5 - Estado: Pendiente

--- preorder ---
  Matrix
  Inception
  El Padrino
  Coco
  El Origen del Planeta de los Simios
  Interstellar
  Joker
  La La Land
  Titanic
  Parásitos
  Whiplash
  Toy Story

--- postorder ---
  El Origen del Planeta de los Simios
  Coco
  El Padrino
  La La Land
  Joker
  Interstellar
  Inception
  Parásitos
  Toy Story
  Whiplash
  Titanic
  Matrix

--- búsquedas ---
Buscar 'matrix': Matrix (1999) - Ciencia ficción - Rating: 9.0 - Estado: Pendiente
Buscar 'zzz': None

4. Comparación de tiempos

TP2 no era obligatorio y no lo hicimos, así que esta tabla compara búsqueda secuencial vs búsqueda en árbol (sin columna de búsqueda binaria). Los tiempos son reales, sacados con algoritmos/medir_tiempos.py, buscando en cada caso el peor escenario posible para la secuencial (el último elemento de la lista):

N elementos	Secuencial (ms)	Árbol BST (ms)
100	0.0095	0.0050
1.000	0.0520	0.0041
10.000	1.2236	0.0045
100.000	7.8804	0.0064

5. Análisis de complejidad
Búsqueda secuencial: O(n). Recorre toda la lista en el peor caso — se nota en la tabla: el tiempo crece de forma prácticamente lineal con N.
Búsqueda en árbol: O(log n) promedio si el árbol está balanceado; O(n) en el peor caso si está degenerado (como una lista, por ejemplo si los datos ya vinieran ordenados al insertarlos). En nuestra prueba el tiempo casi no crece al aumentar N, lo que confirma el comportamiento logarítmico.
Inserción en árbol: O(log n) promedio, O(n) peor caso.
Recorridos (inorder, preorder, postorder): O(n), porque visitan cada nodo una vez.

6. Conclusión

Con 100.000 elementos, la búsqueda secuencial tardó 7.88 ms y la búsqueda en árbol 0.0064 ms: el árbol fue más de 1.200 veces más rápido en ese caso. La diferencia se agranda cuanto más grande es el dataset, porque la secuencial crece linealmente mientras que el árbol casi no se ve afectado. El costo de construir el árbol se paga una sola vez (al cargar los datos), y a partir de ahí todas las búsquedas se benefician. Para nuestra aplicación, donde se buscan películas repetidamente por título, el árbol es claramente la mejor opción.

7. Errores o dudas que tuvimos

Al principio corrimos probar_bst.py directo con python algoritmos/probar_bst.py y tiraba ModuleNotFoundError: No module named 'estructuras', porque Python no encontraba la carpeta estructuras al ejecutar el script desde adentro de algoritmos/. Se soluciona ejecutando el script parado en la raíz del proyecto (no metiéndose a la carpeta algoritmos/).
