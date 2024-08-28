import unittest
from colecciones import ContenedorIterable


class TestColecciones(unittest.TestCase):

    def test_01_iniciar_contenedor_iterable(self):
        contenedor1 = ContenedorIterable()
        contenedor1.agregar(5, 1)
        contenedor1.agregar(3, 1)
        contenedor1.agregar(4, 2)
        contenedor1.agregar(8, 1)
        contenedor1.agregar(10, 2)
        print(contenedor1)

    def test_02_iterar_contenedor_iterable(self):
        contenedor1 = ContenedorIterable()
        contenedor1.agregar(5, 1)
        contenedor1.agregar(3, 1)
        contenedor1.agregar(4, 2)
        contenedor1.agregar(8, 1)
        contenedor1.agregar(10, 2)

        for i in contenedor1:
            print("ski", i)


if __name__ == "__main__":
    unittest.main()
