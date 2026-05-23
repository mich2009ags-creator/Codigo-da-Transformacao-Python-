class Calculadora:
    
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
          raise ValueError("Divisão por zero não é permitida")
        return a / b
        
        import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        """Configuração executada antes de cada teste"""
        self.calc = Calculadora()
    
    def test_somar(self):
        self.assertEqual(self.calc.somar(5, 3), 8)
        self.assertEqual(self.calc.somar(-2, 7), 5)
    
    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)
        self.assertEqual(self.calc.subtrair(0, 5), -5)
    
    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)
        self.assertEqual(self.calc.multiplicar(-2, 5), -10)
    
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(7, 2), 3.5)

if __name__ == '__main__':
    unittest.main()