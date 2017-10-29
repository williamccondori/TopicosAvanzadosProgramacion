import unittest

class Pila:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        if not self.is_full():
            self.items.insert(len(self.items), item)
    def pop(self):
        return self.items.pop(len(self.items) - 1)
    def is_full(self):
        return len(self.items) >= self.tamanio
    def get_size(self):
        return len(self.items)
    def top(self):
        posicion_ultimo = len(self.items) - 1
        return self.items[posicion_ultimo]

    def get(self):
        """
        Mètodo para comprobar el arreglo.
        """
        return self.items

class TestStack(unittest.TestCase):
    def test_crear_pila(self):
        comprobador = ['Manzana', 'Pera', 'Banana', 'Lima', 'Naranjas'] # Este debe de ser el resultado.
        tamanio = 5
        pila = Pila(tamanio)
        pila.push('Manzana')
        pila.push('Pera')
        pila.push('Banana')
        pila.push('Lima')
        pila.push('Naranjas')
        self.assertEqual(pila.get(), comprobador)
    def test_elimnar_pila(self):
        comprobador = ['Manzana', 'Pera', 'Banana', 'Lima'] # Este debe de ser el resultado.
        tamanio = 5
        pila = Pila(tamanio)
        pila.push('Manzana')
        pila.push('Pera')
        pila.push('Banana')
        pila.push('Lima')
        pila.push('Naranjas')
        pila.pop()
        self.assertEqual(pila.get(), comprobador)
    def test_agregar_mas_tamanio(self):
        tamanio = 5
        pila = Pila(tamanio)
        pila.push('Manzana')
        pila.push('Pera')
        pila.push('Banana')
        pila.push('Lima')
        pila.push('Naranjas')
        pila.push('fresa')
        self.assertEqual(pila.get_size(), tamanio)

if __name__ == '__main__':
    unittest.main()
