from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from ui.terminal import cargar_datos, mostrar_menu, listar, filtrar_por_genero, explorar_categorias


def construir_arbol_avl(peliculas):
    """Crea un árbol AVL e inserta todas las películas balanceadamente."""
    arbol = AVL()
    for p in peliculas:
        arbol.insertar(p, clave=lambda e: e.titulo.lower())
    return arbol


def construir_arbol_general(peliculas):
    """Arma la jerarquía Películas -> Género -> Película."""
    arbol = ArbolGeneral()
    arbol.insertar_raiz("Películas")

    nodos_genero = {}
    for p in peliculas:
        if p.genero not in nodos_genero:
            nodos_genero[p.genero] = arbol.agregar_hijo(arbol.raiz, p.genero)
        arbol.agregar_hijo(nodos_genero[p.genero], p.titulo, dato=p)

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
    # Se desempaqueta la tupla (peliculas, arbol) que retorna cargar_datos()
    peliculas, _ = cargar_datos()

    arbol_avl = construir_arbol_avl(peliculas)
    arbol_general = construir_arbol_general(peliculas)

    while True:
        mostrar_menu()
        opcion = input("> Opción: ")

        if opcion == "1":
            buscar_con_arbol(arbol_avl)
        elif opcion == "2":
            listar(peliculas)
        elif opcion == "3":
            filtrar_por_genero(peliculas)
        elif opcion == "4":
            explorar_categorias(arbol_general)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intentá de nuevo.")


if __name__ == "__main__":
    main()
