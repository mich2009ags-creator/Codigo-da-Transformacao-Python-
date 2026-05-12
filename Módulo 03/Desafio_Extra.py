# DESAFIO EXTRA - Menu com while
print("\n=== Menu Interativo ===")

while True:
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", a + b)

    elif opcao == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", a - b)

    elif opcao == "3":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida, tente novamente!")
