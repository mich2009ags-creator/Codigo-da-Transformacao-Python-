"""Atividade 1: Lista de compras"""
    print("\n" + "="*50)
    print("ATIVIDADE 1: LISTA DE COMPRAS")
    print("="*50)
    
    lista = []
    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Visualizar lista")
        print("4. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            item = input("Digite o item para adicionar: ")
            lista.append(item)
            print(f"✓ {item} adicionado!")
            
        elif opcao == "2":
            if lista:
                print("\nLista atual:")
                for i, item in enumerate(lista, 1):
                    print(f"{i}. {item}")
                try:
                    indice = int(input("\nDigite o número do item para remover: "))
                    if 1 <= indice <= len(lista):
                        removido = lista.pop(indice - 1)
                        print(f"✓ {removido} removido!")
                    else:
                        print("❌ Número inválido!")
                except ValueError:
                    print("❌ Digite um número válido!")
            else:
                print("❌ Lista vazia, nada para remover!")
                
        elif opcao == "3":
            if lista:
                print("\n📝 LISTA DE COMPRAS:")
                for i, item in enumerate(lista, 1):
                    print(f"  {i}. {item}")
            else:
                print("📝 Lista vazia!")
                
        elif opcao == "4":
            break
        else: print("❌ Opção inválida!")