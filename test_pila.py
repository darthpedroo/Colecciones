import unittest
from pila import Pila, PilaLlena, PilaVacia

class TestPila(unittest.TestCase):

    def setUp(self):
        self._pila = Pila()
        self._pila.apilar(1)
        self._pila.apilar(2)
        self._pila.apilar(3)
        self._pila.apilar(4)
        self._pila.apilar(5)

    def test_01_pila_apilar(self):
        self._pila.apilar("if iam not back again this time tomorou")
        print("pila:" , self._pila)
    
    def test_02_pila_desapilar(self):
        pila = Pila()
        pila.apilar("mamaaaaaa")
        pila.apilar("u")
        pila.apilar("u")
        pila.apilar("u")
        pila.apilar("didn't mean to make you cry")
        pila.desapilar()

    def test_03_obtener_longitud_pila(self):
        print(self._pila)
        print(len(self._pila))

    def test_04_pila_llena_levanta_error_pila_llena(self):
        pilallena = Pila(2)
        pilallena.apilar("goga")
        pilallena.apilar("retretin")

        with self.assertRaises(PilaLlena):
            pilallena.apilar("galogin")

    def test_05_pila_vacia_levanta_error_pila_vacia(self):
        pilavacia = Pila()
        
        with self.assertRaises(PilaVacia):
            pilavacia.desapilar()

    def test_06_iterar_sobre_pila(self):
        for i in self._pila:
            print(":V", i)






  


if __name__ == "__main__":
    unittest.main()
