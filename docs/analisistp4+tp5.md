# Análisis TP4 + TP5 — Árbol AVL y Árbol General

## 1. ¿Qué resolvimos?
Incorporamos dos estructuras de datos para resolver necesidades distintas del sistema de películas:

| Estructura | Problema que resuelve | Dónde se usa |
| :--- | :--- | :--- |
| **AVL** | Búsquedas por título en $O(\log n)$ garantizado, evitando desbalances cuando los datos entran ordenados. | Opción "Buscar película por título" en el menú. |
| **Árbol General** | Representar la jerarquía natural de categorías/géneros de películas. | Opción "Explorar categorías" en el menú. |

---

## 2. TP4 — Árbol AVL

### 2.1 ¿Por qué AVL y no un BST común?
Un BST convencional degenera en una lista enlazada $O(n)$ si los títulos se insertan en orden alfabético. El AVL soluciona esto aplicando rotaciones automáticas que mantienen la altura balanceada en $O(\log n)$.

### 2.2 Rotaciones implementadas
* **Rotación simple derecha (Izquierda-Izquierda):** Factor de balance $> 1$ y el nuevo nodo está en el hijo izquierdo del izquierdo.
* **Rotación simple izquierda (Derecha-Derecha):** Factor de balance $< -1$ y el nuevo nodo está en el hijo derecho del derecho.
* **Rotación doble izquierda-derecha (Izquierda-Derecha):** Factor de balance $> 1$ pero el hijo izquierdo está cargado a la derecha.
* **Rotación doble derecha-izquierda (Derecha-Izquierda):** Factor de balance $< -1$ pero el hijo derecho está cargado a la izquierda.

### 2.3 Comparación BST vs AVL
*(Inserta datos ordenados A, B, C, D, E, F, G, H, I, J)*

| Métrica | BST común | AVL |
| :--- | :--- | :--- |
| **Altura con 10 datos ordenados** | 10 | 4 |
| **Búsqueda con 10.000 datos ordenados** | [X] ms | [Y] ms |
| **Complejidad peor caso (Búsqueda)** | $O(n)$ | $O(\log n)$ |
| **Complejidad promedio (Inserción)** | $O(\log n)$ | $O(\log n)$ |

### 2.4 Prueba del AVL
Salida de la ejecución de `python estructuras/avl.py`:
```text
[PEGAR AQUÍ LA SALIDA DE LA TERMINAL]
Altura del AVL: [X]
Buscar 'F': Elemento(...)
Buscar 'Z': None