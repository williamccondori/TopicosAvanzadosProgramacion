""" unittest """
import unittest
class StackFactorial(object):
    """
    Clase que contiene las operaciones para hallar el factorial.
    """
    def obtener(self, numero):
        """
        Obtiene el factorial de un número cualquiera.
        """
        if numero == 0:
            return 1
        else:
            return numero * self.obtener(numero - 1)

class TestFactorial(unittest.TestCase):
    """
    Prueba unitaria de factoriales.
    """
    def test_obtener_06(self):
        """
        Comprueba el factorial de un nùmero dado.
        Ejemplo
        -------
        Factorial de 6 = 720
        """
        numero = 6 # Se asigna el valor al número
        factorial = StackFactorial()
        resultado = factorial.obtener(numero)
        self.assertEqual(resultado, 720) # Se compara la posible respuesta
    def test_obtener_10(self):
        """
        Comprueba el factorial de un nùmero dado.
        Ejemplo
        -------
        Factorial de 10 = 3628800
        """
        numero = 10 # Se asigna el valor al número
        factorial = StackFactorial()
        resultado = factorial.obtener(numero)
        self.assertEqual(resultado, 3628800) # Se compara la posible respuesta
    def test_obtener_30(self):
        """
        Comprueba el factorial de un nùmero dado.
        Ejemplo
        -------
        Factorial de 30 = 265252859812191058636308480000000
        """
        numero = 30 # Se asigna el valor al número
        factorial = StackFactorial()
        resultado = factorial.obtener(numero)
        self.assertEqual(resultado, 265252859812191058636308480000000) # Se compara la posible respuesta

if __name__ == '__main__':
    unittest.main()
