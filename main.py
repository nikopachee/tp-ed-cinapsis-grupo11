from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from ui.terminal import cargar_datos, mostrar_menu, listar, filtrar_por_genero


def construir_arbol_avl(peliculas):
    """Crea un árbol AVL e inserta todas las películas balanceadamente."""
    arbol = AVL()
    for p in peliculas:
        arbol.insertar(p, clave=lambda e: e.titulo.lower())
    return arbol


def construir_arbol_categorias():
    """Crea el árbol general con la jerarquía de categorías del dominio."""
    arbol = ArbolGeneral()
    raiz = arbol.insertar_raiz("Películas")

    # Categorías principales
    ciencia = arbol.agregar_hijo(raiz, "Ciencia Ficción")
    accion = arbol.agregar_hijo(raiz, "Acción")
    comedia = arbol.agregar_hijo(raiz, "Comedia")

    # Subcategorías
    arbol.agregar_hijo(ciencia, "Cyberpunk")
    arbol.agregar_hijo(ciencia, "Viajes temporales")
    arbol.agregar_hijo(ciencia, "Inteligencia artificial")

    arbol.agregar_hijo(accion, "Superhéroes")
    arbol.agregar_hijo(accion, "Guerra")

    arbol.agregar_hijo(comedia, "Comedia romántica")
    arbol.agregar_hijo(comedia, "Comedia negra")

    return arbol


def buscar_con_arbol(arbol):
    """Busca una película por título en el árbol AVL en tiempo O(log n)."""
    titulo = input("Título a buscar: ")
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    if resultado:
        print(resultado)
    else:
        print("No se encontró.")


def explorar_categorias(arbol_cat):
    """Muestra la jerarquía de categorías usando el recorrido en amplitud del árbol general."""
    print("\n--- Explorar Categorías (Árbol General - BFS) ---")
    for categoria in arbol_cat.amplitud():
        print(f" • {categoria}")
    print()


def main():
    peliculas = cargar_datos()
    arbol_avl = construir_arbol_avl(peliculas)
    arbol_categorias = construir_arbol_categorias()

    while True:
        mostrar_menu()
        opcion = input("> Opción: ")

        if opcion == "1":
            # Búsqueda optimizada con AVL
            buscar_con_arbol(arbol_avl)
        elif opcion == "2":
            listar(peliculas)
        elif opcion == "3":
            filtrar_por_genero(peliculas)
        elif opcion == "4":
            # Explorar árbol de categorías
            explorar_categorias(arbol_categorias)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intentá de nuevo.")


if __name__ == "__main__":
    main()