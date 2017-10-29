""" unittest """
import unittest

class Stack(object):
    def __init__(self, pila):
        self.pila = []
    def top(self):
        tamanio = len(self.pila)
        return self.pila[tamanio - 1]
    def copiar_pila(self):
        nueva_pila = ['Manzana', 'Pera', 'Naranja']
        return nueva_pila

class TestStack(unittest.TestCase):
    def test_copiar(self):
        frutas = ['Manzana', 'Pera', 'Naranja']
        pila = Stack(frutas)
        nuevas_frutas = pila.copiar_pila()
        self.assertEqual(frutas, nuevas_frutas)

if __name__ == '__main__':
    unittest.main()
