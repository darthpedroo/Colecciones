from collections.abc import Iterable, Iterator


class IteradorDeColeccion(Iterator):
    def __init__(self, coleccion, cant_prioridades):
        self._coleccion = coleccion
        self._indice = 0
        self._curr_type = 1
        # Nose si está bien puesto aca la cantidad de prioridades porque quizas el iterador no sea el mejor lugar para ponerlo
        self._cant_prioridades = cant_prioridades

    def __next__(self):
        if self._curr_type <= self._cant_prioridades:
            if self._indice < len(self._coleccion):
                res = self._coleccion[self._indice]
                self._indice += 1
                if res[1] == self._curr_type:
                    return res
                else:
                    return self.__next__()
            else:
                self._curr_type += 1
                self._indice = 0
                return self.__next__()
        else:
            raise StopIteration


class ContenedorIterable(Iterable):

    def __init__(self):
        self._elementos = []

    def __str__(self):
        return f"El container: {str(self._elementos)}"

    def agregar(self, elemento, tipo_prioridad):
        self._elementos.append((elemento, tipo_prioridad))

    def __iter__(self):
        return IteradorDeColeccion(self._elementos, 9)


class ContenedorIterable2(Iterable):

    def __init__(self) -> None:
        self._elementos = []
        self._current_type = 1
        self._cantidad_prioridades = 9

    def __str__(self):
        return f"El container: {str(self._elementos)}"

    def agregar(self, elemento, tipo_prioridad):
        self._elementos.append((elemento, tipo_prioridad))

    def __iter__(self):
        while self._current_type <= self._cantidad_prioridades:
            for i in self._elementos:
                if i[1] == self._current_type:
                    yield i
            self._current_type += 1


