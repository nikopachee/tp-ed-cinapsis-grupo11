# Análisis TP4 + TP5 — Árbol AVL y Árbol General

## 1. ¿Qué resolvimos?
Incorporamos dos estructuras de datos para resolver necesidades distintas del sistema de películas: 
AVL;Que las búsquedas por título/clave sean siempre rápidas (O(log
n)) incluso cuando los datos se insertan en orden Y se usa en la opcion "buscar" del menu.
Árbol General; Para representar la jerarquía de categorías del dominio Y se usa en la opcion "explorar categorias" en el menu
---

## 2. TP4 — Árbol AVL

### 2.1 ¿Por qué AVL y no un BST común?
Elegimos este tipo(AVL) por sobre un BST ya que este se desbalancea cuando se trata de datos ordenados y pierde efectividad, el AVL se vuelve mucho mejor no solo por la efectividad si no por el uso en cuanto a los nombres de peliculas

### 2.2 Rotaciones implementadas
Rotación simple derecha (Izquierda-Izquierda): Factor de balance > 1 y el nuevo dato va a la izquierda del hijo izquierdo.
Rotación simple izquierda (Derecha-Derecha):Factor de balance < -1 y el nuevo dato va a la derecha del hijo derecho
Rotación doble izquierda-derecha (Izquierda-Derecha): Factor de balance > 1 pero el hijo izquierdo está desbalanceado a la derecha
Rotación doble derecha-izquierda (Derecha-Izquierda): Factor de balance < -1 pero el hijo derecho está desbalanceado a la izquierda

### 2.3 Prueba del AVL
Total de películas insertadas: 12
Altura del árbol AVL: 4

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
  El Origen del Planeta de los Simios
  Coco
  El Padrino
  Joker
  Interstellar
  La La Land
  Titanic
  Parásitos
  Whiplash
  Toy Story

--- postorder ---
  Coco
  El Padrino
  El Origen del Planeta de los Simios
  Interstellar
  La La Land
  Joker
  Inception
  Parásitos
  Toy Story
  Whiplash
  Titanic
  Matrix

--- búsquedas ---
Buscar 'matrix': Matrix (1999) - Ciencia ficción - Rating: 9.0 - Estado: Pendiente
Buscar 'zzz': None
### 2.4 Comparación BST vs AVL
========================================================================
N Elementos | Altura BST | Altura AVL |     BST (ms) |     AVL (ms)
========================================================================
         10 |         10 |          4 |       1.3132 |       0.6363
        100 |        100 |          7 |      24.7254 |       1.0188
       1000 |       1000 |         10 |     239.1036 |       1.4062
      10000 |      10000 |         14 |    2275.1045 |       1.8821
========================================================================
### TP5 Árbol General (N-ario)

### 3.2 ¿Por qué esta jerarquía?
Elegimos la jerarquía Películas → Género → Película porque es la forma más natural en la que alguien piensa su catálogo: primero elige qué tipo de película quiere ver (el género) y después ve las opciones puntuales dentro de esa categoría. La raíz ("Películas") agrupa todo el catálogo, cada género es un nodo intermedio que agrupa sus películas, y cada película es una hoja que además guarda el objeto Pelicula completo (no solo el nombre), para poder mostrar sus datos al encontrarla.

### 3.3 Recorridos implementados
Amplitud (BFS): recorre nivel por nivel, de arriba hacia abajo. Sirve para ver primero todas las categorías antes de entrar a cada una. Profundidad - preorder (DFS): visita primero el nodo y después sus hijos. Sirve para mostrar un género seguido inmediatamente de sus películas. Profundidad - postorder (DFS): visita primero todos los hijos y al final el nodo. Útil si se necesitara calcular algo de abajo hacia arriba (como contar películas por género antes de totalizar). Búsqueda por nombre: recorre el árbol buscando un nodo (categoría o película) por su nombre.

### 3.4 Prueba del arbol general
Altura del árbol general: 3 Cantidad total de nodos: 18

--- Niveles del árbol --- Nivel 0: ['Películas'] Nivel 1: ['Ciencia ficción', 'Romance', 'Drama', 'Animación', 'Musical'] Nivel 2: ['Matrix', 'Inception', 'Interstellar', 'El Origen del Planeta de los Simios', 'Titanic', 'Whiplash', 'El Padrino', 'Joker', 'Parásitos', 'Coco', 'Toy Story', 'La La Land']

--- Recorrido por amplitud (BFS) --- ['Películas', 'Ciencia ficción', 'Romance', 'Drama', 'Animación', 'Musical', 'Matrix', 'Inception', 'Interstellar', 'El Origen del Planeta de los Simios', 'Titanic', 'Whiplash', 'El Padrino', 'Joker', 'Parásitos', 'Coco', 'Toy Story', 'La La Land']

--- Recorrido en profundidad, preorder --- ['Películas', 'Ciencia ficción', 'Matrix', 'Inception', 'Interstellar', 'El Origen del Planeta de los Simios', 'Romance', 'Titanic', 'Drama', 'Whiplash', 'El Padrino', 'Joker', 'Parásitos', 'Animación', 'Coco', 'Toy Story', 'Musical', 'La La Land']

--- Recorrido en profundidad, postorder --- ['Matrix', 'Inception', 'Interstellar', 'El Origen del Planeta de los Simios', 'Ciencia ficción', 'Titanic', 'Romance', 'Whiplash', 'El Padrino', 'Joker', 'Parásitos', 'Drama', 'Coco', 'Toy Story', 'Animación', 'La La Land', 'Musical', 'Películas']

--- Búsquedas --- Buscar categoría 'Drama': Drama Películas en Drama: ['Whiplash', 'El Padrino', 'Joker', 'Parásitos'] Buscar película 'Matrix': Matrix (1999) - Ciencia ficción - Rating: 9.0 - Estado: Pendiente Buscar categoría inexistente 'Terror': None

### 5 Analisis de complejidad 
AVL: Búsqueda, inserción: O(log n) garantizado SIEMPRE, incluso en el peor caso, porque el árbol se reequilibra solo con rotaciones después de cada inserción. Se ve en la comparación: con 10.000 elementos insertados en orden, el BST queda con altura 10.000 (una lista disfrazada de árbol) mientras que el AVL se mantiene en altura 14. Recorridos (inorder, preorder, postorder): O(n), visitan cada nodo una vez.

Árbol General: Búsqueda: O(n) en el peor caso. A diferencia del AVL, acá no hay un criterio de orden que permita descartar ramas enteras: hay que revisar potencialmente todos los nodos hasta encontrar el que se busca. Inserción (agregar_hijo): O(1), porque simplemente se agrega un nodo a la lista de hijos del padre, sin tener que recorrer nada. Recorridos (amplitud, preorder, postorder): O(n), visitan cada nodo una vez.

### 6 Conclusion:
El AVL y el árbol general resuelven problemas distintos y no son intercambiables. El AVL es la elección correcta cuando se necesita buscar rápido por una clave ordenable (el título), y su ventaja se nota exactamente en los casos donde un BST común falla: datos insertados en orden. El árbol general, en cambio, no busca velocidad sino representar una estructura jerárquica que el usuario entiende naturalmente (género → película); su búsqueda es más lenta (O(n)) porque no hay un orden que explotar, pero no es ese su propósito. En la aplicación, cada uno se usa donde corresponde: el AVL en "Buscar" (rapidez), el árbol general en "Explorar categorías" (navegación).

### 7 Errores o dudas que tuvimos: 
cuando intente ejecutar p.titulo.lower() en main Python colapsó porque la clase AVL no tiene un atributo llamado titulo
la solucion fue: peliculas, _ = cargar_datos(), desempaquetás la tupla: la variable peliculas recibe únicamente la lista limpia de objetos Pelicula, y el arbol AVL secundario se descarta en el. Tambien nos paso que, en TP3, que al correr algoritmos/probar_bst.py desde adentro de la carpeta algoritmos/ tirara ModuleNotFoundError: No module named 'estructuras'. Se solucionó agregando sys.path.append(...) al principio del script para que encuentre la raíz del proyecto sin importar desde dónde se lo ejecute. Aplicamos la misma solución en probar_arbol_general.py para TP5.