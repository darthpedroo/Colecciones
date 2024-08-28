from collections.abc import Iterable, Iterator


class IteradorDeColeccion(Iterator):
    def __init__(self, coleccion):
        self._coleccion = coleccion
        self._indice = 0

    def __next__(self):
        if self._indice < len(self._coleccion):
            res = self._coleccion[self._indice]
            self._indice += 1
            if res[1] == 1:
                return res
            else:
                print("DOOPIDOPÍ: ", res)
                # self.__next__()
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
        return IteradorDeColeccion(self._elementos)
