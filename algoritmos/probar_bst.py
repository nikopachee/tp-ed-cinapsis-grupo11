"""
Script de prueba del árbol binario de búsqueda (BST) usando el dominio
real del proyecto (Pelicula), tal como pide el Paso 3 de la Entrega 3.
"""
import sys
import json
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.arbol_binario import ArbolBST
from modelos.pelicula import Pelicula


def cargar_peliculas():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    peliculas = []
    for d in datos:
        peliculas.append(Pelicula(d["titulo"], d["genero"], d["rating"], d["anio"]))
    return peliculas


def main():
    peliculas = cargar_peliculas()

    arbol = ArbolBST()
    for p in peliculas:
        arbol.insertar(p, clave=lambda e: e.titulo.lower())

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for p in arbol.inorder():
        print(" ", p)

    print("\n--- preorder ---")
    for p in arbol.preorder():
        print(" ", p.titulo)

    print("\n--- postorder ---")
    for p in arbol.postorder():
        print(" ", p.titulo)

    print("\n--- búsquedas ---")
    encontrada = arbol.buscar("matrix", clave=lambda e: e.titulo.lower())
    print("Buscar 'matrix':", encontrada)
    no_encontrada = arbol.buscar("zzz", clave=lambda e: e.titulo.lower())
    print("Buscar 'zzz':", no_encontrada)


if __name__ == "__main__":
    main()
