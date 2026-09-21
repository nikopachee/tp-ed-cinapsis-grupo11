from estructuras.arbol_binario import ArbolBST
from ui.terminal import cargar_datos, mostrar_menu, listar, filtrar_por_genero


def construir_arbol(peliculas):
    arbol = ArbolBST()
    for p in peliculas:
        arbol.insertar(p, clave=lambda e: e.titulo.lower())
    return arbol


def buscar_con_arbol(arbol):
    titulo = input("Título a buscar: ")
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    if resultado:
        print(resultado)
    else:
        print("No se encontró.")


def main():
    peliculas = cargar_datos()
    arbol = construir_arbol(peliculas)

    while True:
        mostrar_menu()
        opcion = input("> Opción: ")

        if opcion == "1":
            buscar_con_arbol(arbol)
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
