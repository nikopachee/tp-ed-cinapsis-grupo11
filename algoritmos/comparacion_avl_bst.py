import sys
import os
import time

# Elevar límite de recursión por si el BST degenerado profundiza en N niveles
sys.setrecursionlimit(30000)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL


def medir_busqueda_peor_caso(arbol, objetivo, iteraciones=1000):
    """Mide únicamente el tiempo de búsqueda en milisegundos."""
    inicio = time.time()
    for _ in range(iteraciones):
        arbol.buscar(objetivo, clave=lambda x: x)
    fin = time.time()
    return (fin - inicio) * 1000


def main():
    tamanos = [10, 100, 1_000, 10_000]

    print("=" * 72)
    print(f"{'N Elementos':>11} | {'Altura BST':>10} | {'Altura AVL':>10} | {'BST (ms)':>12} | {'AVL (ms)':>12}")
    print("=" * 72)

    for n in tamanos:
        # Generar datos ordenados para forzar desbalance
        datos_ordenados = [f"Pelicula_{i:05d}" for i in range(n)]
        objetivo = datos_ordenados[-1]  # Peor caso: el último elemento

        bst = ArbolBST()
        avl = AVL()

        for d in datos_ordenados:
            bst.insertar(d, clave=lambda x: x)
            avl.insertar(d, clave=lambda x: x)

        h_bst = bst.altura()
        h_avl = avl.altura()

        t_bst = medir_busqueda_peor_caso(bst, objetivo)
        t_avl = medir_busqueda_peor_caso(avl, objetivo)

        print(f"{n:>11} | {h_bst:>10} | {h_avl:>10} | {t_bst:>12.4f} | {t_avl:>12.4f}")

    print("=" * 72)


if __name__ == "__main__":
    main()