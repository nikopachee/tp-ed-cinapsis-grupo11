import sys
from pathlib import Path
import json

# Fuerza a Python a buscar módulos desde la raíz del repositorio
RAIZ = Path(__file__).resolve().parent.parent
sys.path.append(str(RAIZ))

from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.heap import MaxHeap
from estructuras.grafos import Grafo
from modelos.pelicula import Pelicula


def cargar_datos():
    ruta_json = RAIZ / "datos" / "peliculas.json"
    with open(ruta_json, "r", encoding="utf-8") as f:
        datos = json.load(f)
    peliculas = []
    for d in datos:
        peliculas.append(Pelicula(d["titulo"], d["genero"], d["rating"], d["anio"]))

    arbol = ArbolBST()
    for elemento in peliculas:
        arbol.insertar(elemento, clave=lambda e: e.titulo.lower())

    return peliculas, arbol


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


def construir_heap_ranking(peliculas):
    """Crea un Max-Heap ordenado por rating (y año como desempate)."""
    heap = MaxHeap(clave=lambda p: (p.rating, p.anio))
    for p in peliculas:
        heap.insertar(p)
    return heap


def construir_grafo_similitud(peliculas):
    """Conecta películas según género y década asignando pesos de distancia."""
    grafo = Grafo(dirigido=False, clave=lambda p: p.titulo.lower())
    for i in range(len(peliculas)):
        grafo.agregar_vertice(peliculas[i])
        for j in range(i + 1, len(peliculas)):
            p1, p2 = peliculas[i], peliculas[j]
            mismo_genero = p1.genero.lower() == p2.genero.lower()
            misma_decada = (p1.anio // 10) == (p2.anio // 10)

            if mismo_genero and misma_decada:
                grafo.agregar_arista(p1, p2, peso=1)
            elif mismo_genero:
                grafo.agregar_arista(p1, p2, peso=2)
            elif misma_decada:
                grafo.agregar_arista(p1, p2, peso=3)
    return grafo


def mostrar_menu():
    print("\n" + "=" * 46)
    print("                   CINAPSIS")
    print("=" * 46)
    print("1. Buscar película por título")
    print("2. Ver catálogo completo")
    print("3. Filtrar por género")
    print("4. Explorar catálogo por categorías")
    print("5. Pedir ranking de mejores peliculas")
    print("6. Pedir recomendaciones segun la pelicula vista")
    print("7. Armar maratón")
    print("8. Armar maratón entre dos películas")
    print("0. Salir")
    print("-" * 46)


def buscar_con_arbol(arbol):
    titulo = input("Título a buscar: ")
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    if resultado:
        print(resultado)
    else:
        print("Película no encontrada.")


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


def mostrar_top_n(heap_ranking):
    try:
        n = int(input("¿Cuántas películas querés ver en el ranking?: "))
        if n <= 0:
            print("Ingresá un número mayor a 0.")
            return
    except ValueError:
        print("Tenés que ingresar un número entero.")
        return

    top = heap_ranking.obtener_top_n(n)
    print(f"\n--- TOP {len(top)} MEJORES CALIFICADAS ---")
    for i, p in enumerate(top, 1):
        print(f"{i}. {p.titulo} ({p.anio}) - ★ {p.rating}")


def recomendar_bfs(grafo):
    titulo = input("¿Qué película te gustó?: ")
    recomendaciones = grafo.bfs(titulo.lower(), max_saltos=2)
    if not recomendaciones:
        print("No encontramos esa película o aún no tiene sugerencias asociadas.")
        return

    print(f"\nPorque viste '{titulo}', te recomendamos:")
    for peli, nivel in recomendaciones:
        etiqueta = "Muy similar" if nivel == 1 else "También te puede gustar"
        print(f"- [{etiqueta}] {peli.titulo} ({peli.genero}, {peli.anio}) - ★ {peli.rating}")


def explorar_dfs(grafo):
    titulo = input("¿Con qué película querés arrancar tu maratón?: ")

    try:
        cantidad = int(input("¿Cuántas películas querés incluir?: "))
        if cantidad <= 0:
            print("Ingresá un número mayor a 0.")
            return
    except ValueError:
        print("Tenés que ingresar un número entero.")
        return

    cadena = grafo.dfs(titulo.lower())

    if not cadena:
        print("No encontramos esa película en el catálogo.")
        return

    cadena = cadena[:cantidad]

    print("\n" + "=" * 46)
    print("🎬 MARATÓN TEMÁTICA PERSONALIZADA")
    print("=" * 46)

    print(f"\nPelícula inicial:")
    print(f"{cadena[0].titulo} ({cadena[0].anio})")

    print(f"\nTema predominante:")
    print(cadena[0].genero)

    print(f"\nCantidad solicitada:")
    print(f"{len(cadena)} películas")

    for i, peli in enumerate(cadena, 1):
        print(f"{i}. {peli.titulo} ({peli.anio}) ★ {peli.rating}")

    print("\n" + "-" * 46)


def buscar_camino_minimo(grafo):
    origen = input("¿Con qué película querés empezar?: ")
    destino = input("¿A qué película querés llegar?: ")

    camino, costo = grafo.camino_minimo(
        origen.lower(),
        destino.lower()
    )

    if camino is None:
        print("\nNo encontramos una maratón óptima entre esas dos películas.")
        return

    print("\n" + "=" * 50)
    print("🎬 MARATÓN ÓPTIMA ENTRE PELÍCULAS")
    print("=" * 50)

    print(f"\nOrigen: {camino[0].titulo}")
    print(f"Destino: {camino[-1].titulo}")

    print(f"\nPelículas conectadas: {len(camino)}")
    print(f"Afinidad total del recorrido: {costo}")

    print("\nRecorrido recomendado:\n")

    for i, pelicula in enumerate(camino, 1):
        print(
            f"{i}. {pelicula.titulo} "
            f"({pelicula.genero}, {pelicula.anio}) "
            f"★ {pelicula.rating}"
        )

    print("\n" + "-" * 50)
    #print("Ruta calculada mediante Dijkstra.")
    #print("Se seleccionó el camino de menor costo")
    #print("según género y década de las películas.")


def iniciar_terminal():
    peliculas, _ = cargar_datos()

    arbol_avl = construir_arbol_avl(peliculas)
    arbol_general = construir_arbol_general(peliculas)
    heap_ranking = construir_heap_ranking(peliculas)
    grafo_similitud = construir_grafo_similitud(peliculas)

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
        elif opcion == "5":
            mostrar_top_n(heap_ranking)
        elif opcion == "6":
            recomendar_bfs(grafo_similitud)
        elif opcion == "7":
            explorar_dfs(grafo_similitud)
        elif opcion == "8":
            buscar_camino_minimo(grafo_similitud)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intentá de nuevo.")


if __name__ == "__main__":
    iniciar_terminal()