import unittest
from colecciones import ContenedorIterable


class TestColecciones(unittest.TestCase):



    def test_02_iterar_contenedor_iterable(self):
        contenedor1 = ContenedorIterable()

        contenedor1.agregar(5, 8)
        contenedor1.agregar(3, 1)
        contenedor1.agregar(4, 2)
        contenedor1.agregar(8, 1)
        contenedor1.agregar(10, 5)
        contenedor1.agregar(140, 8)
        contenedor1.agregar(120, 3)
        contenedor1.agregar(10, 3)
        contenedor1.agregar(10, 7)
        contenedor1.agregar(10, 5)
        

        for i in contenedor1:
            print("ski", i)


if __name__ == "__main__":
    unittest.main()
