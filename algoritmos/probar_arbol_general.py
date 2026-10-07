"""
Script de prueba del Árbol General (N-ario) usando el dominio real del
proyecto (Pelicula), tal como pide el Paso 4 de la guía de TP5.

Jerarquía: Películas -> Género -> Película (hoja)
"""
import sys
import json
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from estructuras.arbol_general import ArbolGeneral
from modelos.pelicula import Pelicula


def cargar_peliculas():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    peliculas = []
    for d in datos:
        peliculas.append(Pelicula(d["titulo"], d["genero"], d["rating"], d["anio"]))
    return peliculas


def construir_arbol_general(peliculas):
    """Arma la jerarquía Películas -> Género -> Película."""
    arbol = ArbolGeneral()
    arbol.insertar_raiz("Películas")

    # Guardamos un nodo de categoría por cada género para no duplicarlo
    nodos_genero = {}

    for p in peliculas:
        if p.genero not in nodos_genero:
            nodos_genero[p.genero] = arbol.agregar_hijo(arbol.raiz, p.genero)
        nodo_genero = nodos_genero[p.genero]
        arbol.agregar_hijo(nodo_genero, p.titulo, dato=p)

    return arbol


def main():
    peliculas = cargar_peliculas()
    arbol = construir_arbol_general(peliculas)

    print("Altura del árbol general:", arbol.altura())
    print("Cantidad total de nodos:", arbol.cantidad_nodos())

    print("\n--- Niveles del árbol ---")
    for nivel, nombres in arbol.obtener_niveles().items():
        print(f"Nivel {nivel}: {nombres}")

    print("\n--- Recorrido por amplitud (BFS) ---")
    print(arbol.amplitud())

    print("\n--- Recorrido en profundidad, preorder ---")
    print(arbol.profundidad_preorder())

    print("\n--- Recorrido en profundidad, postorder ---")
    print(arbol.profundidad_postorder())

    print("\n--- Búsquedas ---")
    nodo_genero = arbol.buscar("Drama")
    print("Buscar categoría 'Drama':", nodo_genero.nombre if nodo_genero else None)
    if nodo_genero:
        print("  Películas en Drama:", [h.nombre for h in nodo_genero.hijos])

    nodo_pelicula = arbol.buscar("Matrix")
    print("Buscar película 'Matrix':", nodo_pelicula.dato if nodo_pelicula else None)

    nodo_inexistente = arbol.buscar("Terror")
    print("Buscar categoría inexistente 'Terror':", nodo_inexistente)


if __name__ == "__main__":
    main()
