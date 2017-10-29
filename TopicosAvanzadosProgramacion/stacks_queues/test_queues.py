import unittest

class Cola:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.items = []
    def enqueue(self, item):
        if not self.is_full():
            self.items.insert(len(self.items), item)
    def is_empty(self):
        return self.items == []
    def front(self):
        return self.items[0]
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
    def is_full(self):
        return len(self.items) >= self.tamanio
    def get_size(self):
        return len(self.items)

    def get(self):
        """
        Mètodo para comprobar el arreglo.
        """
        return self.items

class TestQueue(unittest.TestCase):
    def test_crear_cola(self):
        comprobador = ['Manzana', 'Pera', 'Banana', 'Lima', 'Naranjas'] # Este debe de ser el resultado.
        tamanio = 5
        cola = Cola(tamanio)
        cola.enqueue('Manzana')
        cola.enqueue('Pera')
        cola.enqueue('Banana')
        cola.enqueue('Lima')
        cola.enqueue('Naranjas')
        self.assertEqual(cola.get(), comprobador)
    def test_elimnar_cola(self):
        comprobador = ['Pera', 'Banana', 'Lima', 'Naranjas'] # Este debe de ser el resultado.
        tamanio = 5
        cola = Cola(tamanio)
        cola.enqueue('Manzana')
        cola.enqueue('Pera')
        cola.enqueue('Banana')
        cola.enqueue('Lima')
        cola.enqueue('Naranjas')
        cola.dequeue()
        self.assertEqual(cola.get(), comprobador)
    def test_agregar_mas_tamanio(self):
        tamanio = 5
        pila = Cola(tamanio)
        pila.enqueue('Manzana')
        pila.enqueue('Pera')
        pila.enqueue('Banana')
        pila.enqueue('Lima')
        pila.enqueue('Naranjas')
        pila.enqueue('fresa')
        self.assertEqual(pila.get_size(), tamanio)

if __name__ == '__main__':
    unittest.main()
