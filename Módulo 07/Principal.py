principal.py
    
    from utilidades import soma, subtracao, potencia

print("Soma:", soma(10, 5))
print("Subtração:", subtracao(10, 5))
print("Potência:", potencia(2, 3))

datas.py
from datetime import datetime

agora = datetime.now()

print("Hoje é:", agora.strftime("%d/%m/%Y"))
print("Hora:", agora.strftime("%H:%M"))
