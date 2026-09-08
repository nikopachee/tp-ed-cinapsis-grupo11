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
    print("           CINAPSIS - v0.1")
    print("=" * 40)
    print("1. Buscar película por título")
    print("2. Listar todas las películas")
    print("3. Filtrar por género")
    print("0. Salir")
    print("-" * 40)


def buscar(peliculas):
    titulo = input("Título a buscar: ")
    encontradas = False
    for p in peliculas:
        if titulo.lower() in p.titulo.lower():
            print(p)
            encontradas = True
    if not encontradas:
        print("Fin de resultados.")


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
    peliculas = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("> Opción: ")

        if opcion == "1":
            buscar(peliculas)
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