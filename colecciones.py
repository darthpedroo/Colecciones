from collections.abc import Iterable, Iterator


class IteradorDeColeccion(Iterator):
    def __init__(self, coleccion, cant_prioridades):
        self._coleccion = coleccion
        self._indice = 0
        self._curr_type = 1
        self._cant_prioridades = cant_prioridades #Nose si está bien puesto aca la cantidad de prioridades porque quizas el iterador no sea el mejor lugar para ponerlo

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
