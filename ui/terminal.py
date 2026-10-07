import sys
from pathlib import Path

# Fuerza a Python a buscar módulos desde la raíz del repositorio
sys.path.append(str(Path(__file__).resolve().parent.parent))

import json
from estructuras.arbol_binario import ArbolBST  # Importación movida abajo del sys.path
from modelos.pelicula import Pelicula


def cargar_datos():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    peliculas = []
    for d in datos:
        peliculas.append(Pelicula(d["titulo"], d["genero"], d["rating"], d["anio"]))

    arbol = ArbolBST()
    for elemento in peliculas:
        arbol.insertar(elemento, clave=lambda e: e.titulo.lower())

    # Retornamos ambos para usarlos según convenga
    return peliculas, arbol


def mostrar_menu():
    print("=" * 40)
    print("              CINAPSIS")
    print("=" * 40)
    print("1. Buscar película por título")
    print("2. Listar todas las películas")
    print("3. Filtrar por género")
    print("4. Explorar categorías")
    print("0. Salir")
    print("-" * 40)


def listar(peliculas):
    for i, p in enumerate(peliculas, 1):
        print(f"{i}. {p}")


def filtrar_por_genero(peliculas):
    genero = input("Género a filtrar: ")
    encontradas = False
    for p in peliculas:
        if genero.lower() in p.genero.lower():
            print(p)
            encontradas = True
    if not encontradas:
        print("No hay películas de ese género.")


def explorar_categorias(arbol_general):
    """Navega la jerarquía Películas -> Género -> Película del árbol general."""
    print("\nCategorías disponibles:")
    for categoria in arbol_general.raiz.hijos:
        print(f"- {categoria.nombre}")

    nombre_categoria = input("\n¿Qué categoría querés explorar?: ")
    nodo = arbol_general.buscar(nombre_categoria)

    if nodo is None or nodo is arbol_general.raiz:
        print("Categoría no encontrada.")
        return

    if not nodo.hijos:
        print(f"'{nodo.nombre}' no tiene películas cargadas.")
        return

    print(f"\nPelículas en '{nodo.nombre}':")
    for hijo in nodo.hijos:
        print(f"- {hijo.dato}")
