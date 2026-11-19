# Análisis TP8 - BFS y DFS 

## 1 ¿Qué resolvió BFS? 
Necesitábamos recomendar películas similares a una película elegida por el usuario. Para esta tarea utilizamos Breadth First Search (BFS), ya que explora primero los vecinos más cercanos al nodo origen. Esto resulta ideal para recomendación porque las películas más relacionadas son encontradas antes que aquellas que se encuentran más alejadas dentro de la red. 

## 2 Prueba de BFS Película seleccionada: 
¿Qué película te gustó?: Matrix

Porque viste 'Matrix', te recomendamos:
- [Muy similar] Inception (Ciencia ficción, 2010) - ★ 8.8
- [Muy similar] Titanic (Romance, 1997) - ★ 7.8
- [Muy similar] Interstellar (Ciencia ficción, 2014) - ★ 8.6
- [Muy similar] El Origen del Planeta de los Simios (Ciencia ficción, 2011) - ★ 7.6
- [Muy similar] Toy Story (Animación, 1995) - ★ 8.3
- [También te puede gustar] Whiplash (Drama, 2014) - ★ 8.5
- [También te puede gustar] Coco (Animación, 2017) - ★ 8.4
- [También te puede gustar] Joker (Drama, 2019) - ★ 8.4
- [También te puede gustar] La La Land (Musical, 2016) - ★ 8.0
- [También te puede gustar] Parásitos (Drama, 2019) - ★ 8.6

## 3 Complejidad de BFS Tiempo: 
O(V + E) donde: - V = cantidad de vértices. - E = cantidad de aristas. Cada nodo y cada conexión son visitados una sola vez. 

## 4 ¿Qué resolvió DFS? 
Queríamos ofrecer al usuario una forma de descubrir películas relacionadas a través de una exploración profunda del grafo. Para ello implementamos Depth First Search (DFS), que recorre completamente una rama antes de volver atrás y explorar nuevas conexiones. La funcionalidad se presenta como una Maratón Temática Personalizada. El usuario selecciona una película inicial y también la cantidad de títulos que desea incluir en su maratón. 

## 5 Prueba de DFS Película inicial: 
 ¿Con qué película querés arrancar tu maratón?: Matrix
¿Cuántas películas querés incluir?: 5

==============================================
🎬 MARATÓN TEMÁTICA PERSONALIZADA
==============================================

Película inicial:
Matrix (1999)

Tema predominante:
Ciencia ficción

Cantidad solicitada:
5 películas
1. Matrix (1999) ★ 9.0
2. Inception (2010) ★ 8.8
3. Whiplash (2014) ★ 8.5
4. Interstellar (2014) ★ 8.6
5. Coco (2017) ★ 8.4

## 6 Complejidad de DFS Tiempo: 
O(V + E) Cada vértice y cada arista son visitados una sola vez.  

## 7 Conclusión 
BFS resultó ideal para generar recomendaciones cercanas al usuario. DFS permitió construir recorridos largos y coherentes dentro de la red de similitudes, transformándose en la base de la funcionalidad de maratones temáticas personalizadas.