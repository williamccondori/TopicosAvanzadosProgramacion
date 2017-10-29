import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def test_copiar(self):
        frutas = ['Manzana', 'Pera', 'Naranja']
        pila = Stack(frutas)
        nuevas_frutas = pila.copiar_pila()
        self.assertEqual(frutas, nuevas_frutas)

if __name__ == '__main__':
    unittest.main()
