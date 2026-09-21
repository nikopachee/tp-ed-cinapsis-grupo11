import json
from modelos.pelicula import Pelicula


def cargar_datos():
    with open("datos/peliculas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    peliculas = []
    for d in datos:
        peliculas.append(Pelicula(d["titulo"], d["genero"], d["rating"], d["anio"]))
    return peliculas


def mostrar_menu():
    print("=" * 40)
    print("              CINAPSIS")
    print("=" * 40)
    print("1. Buscar película por título")
    print("2. Listar todas las películas")
    print("3. Filtrar por género")
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