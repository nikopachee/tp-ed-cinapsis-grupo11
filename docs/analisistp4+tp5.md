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

### 3.3 Recorridos implementados

### 3.4 Prueba del arbol general

### 5 Analisis de complejidad 

### 6 Conclusion:

### Errores o dudas que tuvimos: 