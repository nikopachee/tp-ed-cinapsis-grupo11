class Pelicula:
    def __init__(self, titulo, genero, rating, anio):
        self._titulo = titulo
        self._genero = genero
        self._rating = rating
        self._anio = anio
        self._estado = "Pendiente"  # todas las películas empiezan como pendientes

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def rating(self):
        return self._rating

    @property
    def anio(self):
        return self._anio

    @property
    def estado(self):
        return self._estado

    def cambiar_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    def __repr__(self):
        return f"{self._titulo} ({self._anio}) - {self._genero} - Rating: {self._rating} - Estado: {self._estado}"
