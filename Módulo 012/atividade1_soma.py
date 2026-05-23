def somar(a, b):
    """Função simples de soma"""
    return a + b
    
    import unittest
from soma import somar

class TestSoma(unittest.TestCase):
    
    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 5)
    
    def test_soma_negativos(self):
        self.assertEqual(somar(-1, -4), -5)
    
    def test_soma_zero(self):
        self.assertEqual(somar(0, 0), 0)
    
    def test_soma_mistos(self):
        self.assertEqual(somar(-5, 10), 5)

if __name__ == '__main__':
    unittest.main()
