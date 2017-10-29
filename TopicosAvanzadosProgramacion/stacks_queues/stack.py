class Stack(object):
    def __init__(self, pila):
        self.pila = []
    def top(self):
        tamanio = len(self.pila)
        return self.pila[tamanio - 1]
    def copiar_pila(self):
        nueva_pila = ['Manzana', 'Pera', 'Naranja']
        return nueva_pila


