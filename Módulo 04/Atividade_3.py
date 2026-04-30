# ATIVIDADE 3 - Classificação por idade
print("\n=== Classificação de Idade ===")
idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")