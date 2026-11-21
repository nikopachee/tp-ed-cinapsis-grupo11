# Requerimientos — Cinapsis

Cinapsis es un sistema de recomendación de películas por terminal. Permite buscar y explorar títulos por nombre, género o categoría, consultar los mejores rankings, recibir recomendaciones a partir de una película que gustó y armar maratones.

## 1. Requerimientos funcionales (RF)

| ID | Requerimiento | Estructura / algoritmo | Opción del menú |
|---|---|---|---|
| RF1 | Cargar el catálogo de películas desde un archivo JSON al iniciar. | Lista de objetos `Pelicula` | (al iniciar) |
| RF2 | Buscar una película por su título. | AVL ordenado por título | 1 |
| RF3 | Ver el catálogo completo, numerado. | Lista | 2 |
| RF4 | Filtrar las películas por género. | Recorrido de la lista | 3 |
| RF5 | Explorar el catálogo por categorías (género) y ver las películas de cada una. | Árbol general (Películas → Género → Película) | 4 |
| RF6 | Ver el ranking de las N mejores películas según su rating (y año como desempate). | Max-Heap | 5 |
| RF7 | Recibir recomendaciones a partir de una película que le gustó al usuario, distinguiendo "muy similar" (1 salto) de "también te puede gustar" (2 saltos). | Grafo de similitud + BFS | 6 |
| RF8 | Armar una maratón temática de N películas a partir de una película inicial. | Grafo de similitud + DFS | 7 |
| RF9 | Armar una maratón entre dos películas, eligiendo el recorrido de menor costo (mayor afinidad). | Grafo de similitud + Dijkstra | 8 |
| RF10 | Validar las entradas del usuario (números inválidos, títulos inexistentes) mostrando un mensaje claro sin que el programa se interrumpa. | — | todas |

## 2. Requerimientos no funcionales (RNF)

| ID | Requerimiento |
|---|---|
| RNF1 | **Eficiencia de búsqueda:** la búsqueda por título debe ser O(log n), garantizada aun cuando los datos se carguen ordenados (por eso se usa AVL y no un BST común). |
| RNF2 | **Ranking:** consultar el Top-N no debe alterar el ranking original (se trabaja sobre una copia del heap). |
| RNF3 | **Implementación propia:** BST, AVL, árbol general, heap y grafo están implementados por el equipo, sin librerías que resuelvan el objetivo académico. |
| RNF4 | **Portabilidad:** corre con Python 3 sin instalar dependencias externas, desde cualquier carpeta (las rutas se resuelven a partir de la raíz del repositorio). |
| RNF5 | **Usabilidad:** interfaz de terminal con un menú numerado único y mensajes en español. |
| RNF6 | **Capacidad:** debe poder manejar un catálogo de al menos 1.000 películas sin demora perceptible al iniciar ni al consultar. |
| RNF7 | **Mantenibilidad:** cada estructura vive en su propio módulo (`estructuras/`), separada de los modelos del dominio y de la interfaz. |
| RNF8 | **Verificabilidad:** las estructuras cuentan con pruebas unitarias (`tests/`). |

## 3. Alcance y fuera de alcance

**Dentro del alcance**
- Consulta, exploración y recomendación sobre un catálogo fijo de películas cargado desde JSON.
- Interfaz de terminal.

**Fuera del alcance**
- Alta, baja o modificación de películas en tiempo de ejecución (el JSON es de solo lectura).
- Usuarios, perfiles o historial personal de películas vistas.
- Persistencia de preferencias entre ejecuciones.
- Interfaz gráfica o web.
- Obtención de datos desde servicios externos o APIs.

## 4. Limitaciones conocidas

- El grafo de similitud se arma comparando todos los pares de películas, por lo que su construcción es O(n²) en tiempo y puede tener hasta O(n²) aristas. Es adecuado para catálogos de cientos o pocos miles de películas, pero no escalaría a cientos de miles sin cambiar el criterio de conexión (por ejemplo, conectar solo con los k vecinos más cercanos).
- Las búsquedas por título comparan el texto completo en minúsculas; hay que escribir el título exacto (con sus tildes).
