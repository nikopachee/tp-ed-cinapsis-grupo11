class MaxHeap:
    def __init__(self, clave=lambda x: x):
        self.datos = []
        self.clave = clave

    def __len__(self):
        return len(self.datos)

    def esta_vacio(self):
        return len(self.datos) == 0

    def ver_max(self):
        """Retorna el elemento de mayor prioridad sin extraerlo en O(1)."""
        return self.datos[0] if not self.esta_vacio() else None

    def insertar(self, item):
        """Inserta un elemento y restaura la propiedad de Max-Heap en O(log n)."""
        self.datos.append(item)
        self._flotar(len(self.datos) - 1)

    def extraer_max(self):
        """Extrae y retorna el elemento de mayor prioridad en O(log n)."""
        if self.esta_vacio():
            return None
        if len(self.datos) == 1:
            return self.datos.pop()

        maximo = self.datos[0]
        self.datos[0] = self.datos.pop()
        self._hundir(0)
        return maximo

    def _flotar(self, indice):
        padre = (indice - 1) // 2
        while indice > 0 and self.clave(self.datos[indice]) > self.clave(self.datos[padre]):
            self.datos[indice], self.datos[padre] = self.datos[padre], self.datos[indice]
            indice = padre
            padre = (indice - 1) // 2

    def _hundir(self, indice):
        n = len(self.datos)
        while True:
            mayor = indice
            izq = 2 * indice + 1
            der = 2 * indice + 2

            if izq < n and self.clave(self.datos[izq]) > self.clave(self.datos[mayor]):
                mayor = izq
            if der < n and self.clave(self.datos[der]) > self.clave(self.datos[mayor]):
                mayor = der

            if mayor != indice:
                self.datos[indice], self.datos[mayor] = self.datos[mayor], self.datos[indice]
                indice = mayor
            else:
                break

    def obtener_top_n(self, n):
        """Retorna los N mejores elementos sin modificar el heap original."""
        copia = MaxHeap(clave=self.clave)
        copia.datos = list(self.datos)
        resultado = []
        for _ in range(min(n, len(copia))):
            resultado.append(copia.extraer_max())
        return resultado