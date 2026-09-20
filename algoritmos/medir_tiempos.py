import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import time
from estructuras.arbol_binario import ArbolBST


def medir_arbol(lista, titulo):
    """Mide la búsqueda en árbol sobre la lista dada."""
    arbol = ArbolBST()
    for e in lista:
        arbol.insertar(e, clave=lambda e: e.titulo.lower())
    inicio = time.time()
    resultado = arbol.buscar(titulo.lower(), clave=lambda e: e.titulo.lower())
    fin = time.time()
    return (fin - inicio) * 1000  # milisegundos