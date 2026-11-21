# Diagrama de clases

> Actualizado en TP10 con la implementación completa (v1 + AVL, árbol general, heap y grafo).

```mermaid
classDiagram
    class Pelicula {
        -titulo: str
        -genero: str
        -rating: float
        -anio: int
        -estado: str
        +titulo() str
        +genero() str
        +rating() float
        +anio() int
        +estado() str
        +cambiar_estado(nuevo_estado) None
        +repr() str
    }

    class NodoArbol {
        +dato
        +izquierdo: NodoArbol
        +derecho: NodoArbol
    }

    class ArbolBST {
        -raiz: NodoArbol
        +insertar(dato, clave) None
        +buscar(valor, clave) Pelicula
        +inorder() list
        +preorder() list
        +postorder() list
        +altura() int
        +esta_vacio() bool
    }

    class NodoAVL {
        +dato
        +izquierdo: NodoAVL
        +derecho: NodoAVL
        +altura: int
    }

    class AVL {
        -raiz: NodoAVL
        +insertar(dato, clave) None
        +buscar(valor, clave) Pelicula
        +inorder() list
        +preorder() list
        +postorder() list
        +altura() int
        +esta_vacio() bool
        +len() int
        -_rotacion_izquierda(z) NodoAVL
        -_rotacion_derecha(z) NodoAVL
        -_rotacion_izquierda_derecha(nodo) NodoAVL
        -_rotacion_derecha_izquierda(nodo) NodoAVL
    }

    class NodoGeneral {
        +nombre: str
        +dato
        +hijos: list
    }

    class ArbolGeneral {
        -raiz: NodoGeneral
        +insertar_raiz(nombre) NodoGeneral
        +agregar_hijo(nodo_padre, nombre, dato) NodoGeneral
        +buscar(nombre) NodoGeneral
        +amplitud() list
        +profundidad_preorder() list
        +profundidad_postorder() list
        +obtener_niveles() dict
        +altura() int
        +cantidad_nodos() int
    }

    class MaxHeap {
        -datos: list
        -clave: function
        +insertar(item) None
        +extraer_max() Pelicula
        +ver_max() Pelicula
        +obtener_top_n(n) list
        +esta_vacio() bool
        +len() int
    }

    class Grafo {
        -dirigido: bool
        -clave: function
        -adyacencia: dict
        +agregar_vertice(elemento) None
        +agregar_arista(origen, destino, peso) None
        +bfs(id_origen, max_saltos) list
        +dfs(id_origen) list
        +camino_minimo(id_origen, id_destino) tuple
    }

    class Terminal {
        <<modulo ui/terminal.py>>
        +iniciar_terminal() None
        +cargar_datos() list
        +construir_arbol_avl(peliculas) AVL
        +construir_arbol_general(peliculas) ArbolGeneral
        +construir_heap_ranking(peliculas) MaxHeap
        +construir_grafo_similitud(peliculas) Grafo
        +mostrar_menu() None
    }

    ArbolBST "1" *-- "0..*" NodoArbol : raiz
    AVL "1" *-- "0..*" NodoAVL : raiz
    ArbolGeneral "1" *-- "0..*" NodoGeneral : raiz
    NodoGeneral "1" *-- "0..*" NodoGeneral : hijos

    NodoArbol o-- Pelicula : dato
    NodoAVL o-- Pelicula : dato
    NodoGeneral o-- Pelicula : dato (solo hojas)
    MaxHeap "1" o-- "0..*" Pelicula : ordena por rating
    Grafo "1" o-- "0..*" Pelicula : vertices

    Terminal ..> AVL : usa (opcion 1)
    Terminal ..> ArbolGeneral : usa (opcion 4)
    Terminal ..> MaxHeap : usa (opcion 5)
    Terminal ..> Grafo : usa (opciones 6, 7 y 8)
    Terminal ..> ArbolBST : carga inicial
    Terminal ..> Pelicula : crea
```

## Cómo leer las relaciones

- **Composición (`*--`):** el nodo no existe fuera de su árbol. Si se destruye el árbol, se destruyen sus nodos (`AVL` → `NodoAVL`, `ArbolGeneral` → `NodoGeneral`, etc.).
- **Agregación (`o--`):** las estructuras *contienen referencias* a objetos `Pelicula`, pero las películas existen independientemente de ellas: la misma `Pelicula` está a la vez en el AVL, en el árbol general, en el heap y en el grafo, sin duplicarse.
- **Dependencia (`..>`):** `Terminal` construye y usa las estructuras, pero no forma parte de ellas. La estructura no conoce a la terminal.
- **Herencia:** no se usa. Cada estructura es independiente; el criterio de orden se le pasa como función (`clave`), lo que permite reutilizar las mismas clases con cualquier tipo de dato.
