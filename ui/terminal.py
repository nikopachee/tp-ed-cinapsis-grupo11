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
    print("           CINAPSIS - v0.1")
    print("=" * 40)
    print("1. Buscar película por título")
    print("2. Listar todas las películas")
    print("3. Filtrar por género")
    print("0. Salir")
    print("-" * 40)


# ---------------------------------------------------------
# CAMBIO 2.4: Ahora recibe 'arbol' y usa la búsqueda del BST
# ---------------------------------------------------------
def buscar(arbol):
    titulo = input("Título a buscar: ")

    # Búsqueda usando el árbol BST
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())

    if resultado:
        print(resultado)
    else:
        print("Fin de resultados / Película no encontrada.")


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


def main():
    # Recibimos la lista y el árbol cargados
    peliculas, arbol = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("> Opción: ")

        if opcion == "1":
            # Le pasamos el árbol a la función buscar
            buscar(arbol)
        elif opcion == "2":
            listar(peliculas)
        elif opcion == "3":
            filtrar_por_genero(peliculas)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intentá de nuevo.")


if __name__ == "__main__":
    main()