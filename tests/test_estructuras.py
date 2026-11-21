"""
Pruebas unitarias de las estructuras de datos de Cinapsis.

Ejecutar desde la raíz del repositorio:
    python -m unittest discover tests -v
o directamente:
    python tests/test_estructuras.py
"""
import sys
import random
import unittest
from pathlib import Path

# Permite importar los módulos desde la raíz del repositorio
sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.heap import MaxHeap
from estructuras.grafos import Grafo
from modelos.pelicula import Pelicula


def identidad(x):
    return x


class TestArbolBST(unittest.TestCase):
    def test_insertar_y_buscar(self):
        arbol = ArbolBST()
        for n in [50, 30, 70, 20, 40]:
            arbol.insertar(n, clave=identidad)
        self.assertEqual(arbol.buscar(40, clave=identidad), 40)
        self.assertIsNone(arbol.buscar(99, clave=identidad))

    def test_inorder_devuelve_ordenado(self):
        arbol = ArbolBST()
        datos = [50, 30, 70, 20, 40, 60, 80]
        for n in datos:
            arbol.insertar(n, clave=identidad)
        self.assertEqual(arbol.inorder(), sorted(datos))

    def test_datos_ordenados_degeneran_en_lista(self):
        """Con datos ya ordenados el BST común queda con altura = n."""
        arbol = ArbolBST()
        for n in range(1, 51):
            arbol.insertar(n, clave=identidad)
        self.assertEqual(arbol.altura(), 50)


class TestAVL(unittest.TestCase):
    def test_rotacion_simple_derecha(self):
        avl = AVL()
        for n in [3, 2, 1]:  # caso izquierda-izquierda
            avl.insertar(n, clave=identidad)
        self.assertEqual(avl.raiz.dato, 2)
        self.assertEqual(avl.altura(), 2)

    def test_rotacion_simple_izquierda(self):
        avl = AVL()
        for n in [1, 2, 3]:  # caso derecha-derecha
            avl.insertar(n, clave=identidad)
        self.assertEqual(avl.raiz.dato, 2)
        self.assertEqual(avl.altura(), 2)

    def test_rotacion_doble_izquierda_derecha(self):
        avl = AVL()
        for n in [3, 1, 2]:
            avl.insertar(n, clave=identidad)
        self.assertEqual(avl.raiz.dato, 2)
        self.assertEqual(avl.altura(), 2)

    def test_rotacion_doble_derecha_izquierda(self):
        avl = AVL()
        for n in [1, 3, 2]:
            avl.insertar(n, clave=identidad)
        self.assertEqual(avl.raiz.dato, 2)
        self.assertEqual(avl.altura(), 2)

    def test_datos_ordenados_quedan_balanceados(self):
        """El caso donde el BST falla: el AVL mantiene altura logarítmica."""
        avl = AVL()
        for n in range(1, 1001):
            avl.insertar(n, clave=identidad)
        self.assertLessEqual(avl.altura(), 14)

    def test_inorder_ordenado_con_datos_mezclados(self):
        random.seed(1)
        datos = random.sample(range(10000), 200)
        avl = AVL()
        for n in datos:
            avl.insertar(n, clave=identidad)
        self.assertEqual(avl.inorder(), sorted(datos))

    def test_buscar_existente_e_inexistente(self):
        avl = AVL()
        for n in [10, 20, 30, 40, 50]:
            avl.insertar(n, clave=identidad)
        self.assertEqual(avl.buscar(30, clave=identidad), 30)
        self.assertIsNone(avl.buscar(35, clave=identidad))

    def test_duplicado_no_se_inserta(self):
        avl = AVL()
        avl.insertar(5, clave=identidad)
        avl.insertar(5, clave=identidad)
        self.assertEqual(len(avl), 1)

    def test_buscar_pelicula_por_titulo(self):
        avl = AVL()
        matrix = Pelicula("Matrix", "Ciencia ficción", 9.0, 1999)
        avl.insertar(matrix, clave=lambda p: p.titulo.lower())
        avl.insertar(Pelicula("Coco", "Animación", 8.4, 2017),
                     clave=lambda p: p.titulo.lower())
        encontrada = avl.buscar("matrix", clave=lambda p: p.titulo.lower())
        self.assertIs(encontrada, matrix)


class TestArbolGeneral(unittest.TestCase):
    def setUp(self):
        #  Películas
        #  ├── Drama
        #  │   ├── Joker
        #  │   └── Whiplash
        #  └── Animación
        #      └── Coco
        self.arbol = ArbolGeneral()
        raiz = self.arbol.insertar_raiz("Películas")
        drama = self.arbol.agregar_hijo(raiz, "Drama")
        animacion = self.arbol.agregar_hijo(raiz, "Animación")
        self.arbol.agregar_hijo(drama, "Joker")
        self.arbol.agregar_hijo(drama, "Whiplash")
        self.arbol.agregar_hijo(animacion, "Coco")

    def test_amplitud(self):
        self.assertEqual(
            self.arbol.amplitud(),
            ["Películas", "Drama", "Animación", "Joker", "Whiplash", "Coco"])

    def test_preorder(self):
        self.assertEqual(
            self.arbol.profundidad_preorder(),
            ["Películas", "Drama", "Joker", "Whiplash", "Animación", "Coco"])

    def test_postorder(self):
        self.assertEqual(
            self.arbol.profundidad_postorder(),
            ["Joker", "Whiplash", "Drama", "Coco", "Animación", "Películas"])

    def test_buscar_ignora_mayusculas(self):
        nodo = self.arbol.buscar("drama")
        self.assertIsNotNone(nodo)
        self.assertEqual(len(nodo.hijos), 2)

    def test_buscar_inexistente(self):
        self.assertIsNone(self.arbol.buscar("Terror"))

    def test_altura_y_cantidad_de_nodos(self):
        self.assertEqual(self.arbol.altura(), 3)
        self.assertEqual(self.arbol.cantidad_nodos(), 6)

    def test_obtener_niveles(self):
        niveles = self.arbol.obtener_niveles()
        self.assertEqual(niveles[0], ["Películas"])
        self.assertEqual(niveles[1], ["Drama", "Animación"])
        self.assertEqual(niveles[2], ["Joker", "Whiplash", "Coco"])

    def test_arbol_vacio(self):
        vacio = ArbolGeneral()
        self.assertEqual(vacio.amplitud(), [])
        self.assertIsNone(vacio.buscar("x"))
        self.assertEqual(vacio.altura(), 0)


class TestMaxHeap(unittest.TestCase):
    def test_extrae_en_orden_descendente(self):
        random.seed(2)
        datos = random.sample(range(1000), 100)
        heap = MaxHeap()
        for n in datos:
            heap.insertar(n)
        extraidos = [heap.extraer_max() for _ in range(len(datos))]
        self.assertEqual(extraidos, sorted(datos, reverse=True))

    def test_ver_max_no_extrae(self):
        heap = MaxHeap()
        for n in [3, 9, 5]:
            heap.insertar(n)
        self.assertEqual(heap.ver_max(), 9)
        self.assertEqual(len(heap), 3)

    def test_top_n_no_modifica_el_heap(self):
        heap = MaxHeap()
        for n in [4, 8, 1, 9, 6]:
            heap.insertar(n)
        self.assertEqual(heap.obtener_top_n(3), [9, 8, 6])
        self.assertEqual(len(heap), 5)

    def test_top_n_mayor_a_la_cantidad_de_elementos(self):
        heap = MaxHeap()
        for n in [1, 2]:
            heap.insertar(n)
        self.assertEqual(heap.obtener_top_n(10), [2, 1])

    def test_heap_vacio(self):
        heap = MaxHeap()
        self.assertTrue(heap.esta_vacio())
        self.assertIsNone(heap.ver_max())
        self.assertIsNone(heap.extraer_max())

    def test_ranking_de_peliculas_con_desempate_por_anio(self):
        """Mismo rating: gana la película más reciente (clave = (rating, anio))."""
        heap = MaxHeap(clave=lambda p: (p.rating, p.anio))
        vieja = Pelicula("Vieja", "Drama", 8.0, 1990)
        nueva = Pelicula("Nueva", "Drama", 8.0, 2020)
        mejor = Pelicula("Mejor", "Drama", 9.0, 2000)
        for p in [vieja, nueva, mejor]:
            heap.insertar(p)
        self.assertEqual(heap.obtener_top_n(3), [mejor, nueva, vieja])


class TestGrafo(unittest.TestCase):
    def setUp(self):
        # A --1-- B --1-- C --1-- D      y además A --5-- C
        self.g = Grafo(dirigido=False)
        self.g.agregar_arista("A", "B", 1)
        self.g.agregar_arista("B", "C", 1)
        self.g.agregar_arista("A", "C", 5)
        self.g.agregar_arista("C", "D", 1)

    def test_grafo_no_dirigido_es_simetrico(self):
        self.assertIn("A", self.g.adyacencia["B"]["vecinos"])
        self.assertIn("B", self.g.adyacencia["A"]["vecinos"])

    def test_no_se_crean_lazos(self):
        self.g.agregar_arista("A", "A", 1)
        self.assertNotIn("A", self.g.adyacencia["A"]["vecinos"])

    def test_bfs_niveles(self):
        resultado = dict(self.g.bfs("A"))
        self.assertEqual(resultado, {"B": 1, "C": 1, "D": 2})

    def test_bfs_con_limite_de_saltos(self):
        resultado = dict(self.g.bfs("A", max_saltos=1))
        self.assertEqual(resultado, {"B": 1, "C": 1})

    def test_bfs_origen_inexistente(self):
        self.assertEqual(self.g.bfs("Z"), [])

    def test_dfs_visita_todos_los_alcanzables(self):
        recorrido = self.g.dfs("A")
        self.assertEqual(recorrido[0], "A")
        self.assertEqual(sorted(recorrido), ["A", "B", "C", "D"])

    def test_dfs_origen_inexistente(self):
        self.assertEqual(self.g.dfs("Z"), [])

    def test_dijkstra_prefiere_el_camino_barato(self):
        """A->C directo cuesta 5, pero A->B->C cuesta 2."""
        camino, costo = self.g.camino_minimo("A", "C")
        self.assertEqual(camino, ["A", "B", "C"])
        self.assertEqual(costo, 2)

    def test_dijkstra_camino_largo(self):
        camino, costo = self.g.camino_minimo("A", "D")
        self.assertEqual(camino, ["A", "B", "C", "D"])
        self.assertEqual(costo, 3)

    def test_dijkstra_sin_conexion(self):
        self.g.agregar_vertice("E")  # vértice aislado
        camino, costo = self.g.camino_minimo("A", "E")
        self.assertIsNone(camino)
        self.assertEqual(costo, float("inf"))

    def test_dijkstra_vertice_inexistente(self):
        camino, costo = self.g.camino_minimo("A", "Z")
        self.assertIsNone(camino)
        self.assertEqual(costo, float("inf"))

    def test_grafo_de_peliculas_con_clave_por_titulo(self):
        g = Grafo(dirigido=False, clave=lambda p: p.titulo.lower())
        a = Pelicula("Matrix", "Ciencia ficción", 9.0, 1999)
        b = Pelicula("Inception", "Ciencia ficción", 8.8, 2010)
        g.agregar_arista(a, b, peso=2)
        recomendadas = g.bfs("matrix", max_saltos=2)
        self.assertEqual(recomendadas, [(b, 1)])


if __name__ == "__main__":
    unittest.main(verbosity=2)