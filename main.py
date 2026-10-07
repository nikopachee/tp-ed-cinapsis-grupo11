from estructuras.avl import AVL
from ui.terminal import cargar_datos, mostrar_menu, listar, filtrar_por_genero


def construir_arbol_avl(peliculas):
    """Crea un árbol AVL e inserta todas las películas balanceadamente."""
    arbol = AVL()
    for p in peliculas:
        arbol.insertar(p, clave=lambda e: e.titulo.lower())
    return arbol


def buscar_con_arbol(arbol):
    """Busca una película por título en el árbol AVL en tiempo O(log n)."""
    titulo = input("Título a buscar: ")
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    if resultado:
        print(resultado)
    else:
        print("Fin de resultados / Película no encontrada.")


def main():
    # Se desempaqueta la tupla (peliculas, arbol) que retorna cargar_datos() porque antes python colapsaba y tiraba un error
    peliculas, _ = cargar_datos()

    arbol_avl = construir_arbol_avl(peliculas)

    while True:
        mostrar_menu()
        opcion = input("> Opción: ")

        if opcion == "1":
        
            buscar_con_arbol(arbol_avl)
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