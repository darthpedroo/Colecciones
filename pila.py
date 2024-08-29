from collections.abc import Iterable, Iterator

class PilaLlena(Exception):
    def __init__(self):
        super().__init__("La pila está llena")

class PilaVacia(Exception):
    def __init__(self):
        super().__init__("La pila está Vacía")




class Pila(Iterable):
    def __init__(self, cantidad_maxima_elementos_pila=20):
        self._pila = []
        self._cantidad_maxima_elementos_pila = cantidad_maxima_elementos_pila

    def apilar(self,elemento):
        if len(self._pila) >= self._cantidad_maxima_elementos_pila:
            raise PilaLlena()    
        self._pila.append(elemento)
        
    def desapilar(self):
        if len(self._pila) <= 0:
            raise PilaVacia()
        return self._pila.pop(-1)

    def __len__(self):
        return len(self._pila)
    
    def __str__(self):
        return str(self._pila)

    def __iter__(self):
        for elemento in reversed(self._pila):
            yield elemento

    def __reversed__(self):
        for elemento in self._pila:
            yield elemento
