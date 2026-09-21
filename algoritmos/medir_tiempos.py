"""
medir_tiempos.py — Compara búsqueda secuencial vs búsqueda en árbol BST.

Genera datos sintéticos (títulos únicos) para poder medir con tamaños
grandes, ya que el dataset real del proyecto (datos/peliculas.json) es
chico. La construcción del árbol NO se mide, solo la búsqueda.
"""
import sys
import time
import random
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.arbol_binario import ArbolBST
from modelos.pelicula import Pelicula


def generar_peliculas(n):
    """Genera n películas con títulos únicos, en orden aleatorio."""
    peliculas = [
        Pelicula(f"Pelicula {i:06d}", "Genero", 5.0, 2000)
        for i in range(n)
    ]
    random.shuffle(peliculas)
    return peliculas


def busqueda_secuencial(lista, titulo):
    """Recorre la lista de principio a fin buscando el título."""
    for p in lista:
        if p.titulo.lower() == titulo.lower():
            return p
    return None


def medir_secuencial(lista, titulo):
    inicio = time.time()
    busqueda_secuencial(lista, titulo)
    fin = time.time()
    return (fin - inicio) * 1000  # milisegundos


def medir_arbol(lista, titulo):
    """Mide la búsqueda en árbol sobre la lista dada.

    El árbol se construye UNA vez y NO se mide: solo se cronometra
    la búsqueda.
    """
    arbol = ArbolBST()
    for e in lista:
        arbol.insertar(e, clave=lambda e: e.titulo.lower())

    inicio = time.time()
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    fin = time.time()
    return (fin - inicio) * 1000  # milisegundos


def main():
    tamanos = [100, 1_000, 10_000, 100_000]

    print(f"{'N elementos':>12} | {'Secuencial (ms)':>16} | {'Árbol (ms)':>12}")
    print("-" * 46)

    for n in tamanos:
        lista = generar_peliculas(n)
        # Buscamos el último elemento generado: es el peor caso posible
        # para la búsqueda secuencial (recorre toda la lista).
        titulo_buscado = f"Pelicula {n - 1:06d}"

        tiempo_secuencial = medir_secuencial(lista, titulo_buscado)
        tiempo_arbol = medir_arbol(lista, titulo_buscado)

        print(f"{n:>12} | {tiempo_secuencial:>16.4f} | {tiempo_arbol:>12.4f}")


if __name__ == "__main__":
    main()
