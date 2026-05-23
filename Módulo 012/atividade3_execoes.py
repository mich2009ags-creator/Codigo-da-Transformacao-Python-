class CalculadoraSegura:
    
    def somar(self, a, b):
        self._validar_numeros(a, b)
        return a + b
    
    def dividir(self, a, b):
        self._validar_numeros(a, b)
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b
    
    def _validar_numeros(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os valores devem ser números")