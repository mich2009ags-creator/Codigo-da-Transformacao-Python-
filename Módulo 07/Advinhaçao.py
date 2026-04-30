adivinhação.py
import random

numero_secreto = random.randint(1, 100)

palpite = int(input("Digite um número entre 1 e 100: "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Errou!")
    print("O número era:", numero_secreto)

