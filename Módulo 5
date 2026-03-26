def atividade1_lista_compras():
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
        else:
            print("❌ Opção inválida!")


def atividade2_dados_aluno():
    """Atividade 2: Dados do aluno em dicionário"""
    print("\n" + "="*50)
    print("ATIVIDADE 2: DADOS DO ALUNO")
    print("="*50)
    
    aluno = {}
    
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    aluno["notas"] = notas
    aluno["media"] = sum(notas) / len(notas)
    
    print("\n" + "-"*30)
    print("📊 DADOS DO ALUNO:")
    print("-"*30)
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    
    if aluno["media"] >= 7:
        print("Status: ✅ APROVADO")
    elif aluno["media"] >= 5:
        print("Status: ⚠️ RECUPERAÇÃO")
    else:
        print("Status: ❌ REPROVADO")
    
    input("\nPressione Enter para continuar...")


def atividade3_pares_impares():
    """Atividade 3: Separar pares e ímpares"""
    print("\n" + "="*50)
    print("ATIVIDADE 3: PARES E ÍMPARES")
    print("="*50)
    
    # Conjunto de números
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    
    pares = []
    impares = []
    
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    print(f"\n📊 Conjunto de números: {sorted(numeros)}")
    print(f"\n✅ Números pares ({len(pares)} números): {pares}")
    print(f"❌ Números ímpares ({len(impares)} números): {impares}")
    
    input("\nPressione Enter para continuar...")


def atividade4_agenda():
    """Atividade 4 (Extra): Agenda de contatos"""
    print("\n" + "="*50)
    print("ATIVIDADE 4: AGENDA DE CONTATOS")
    print("="*50)
    
    agenda = {}
    
    while True:
        print("\n--- Agenda de Contatos ---")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Visualizar todos os contatos")
        print("5. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone: ")
            agenda[nome] = telefone
            print(f"✓ Contato {nome} adicionado!")
            
        elif opcao == "2":
            if agenda:
                nome = input("Digite o nome do contato para remover: ")
                if nome in agenda:
                    del agenda[nome]
                    print(f"✓ Contato {nome} removido!")
                else:
                    print("❌ Contato não encontrado!")
            else:
                print("❌ Agenda vazia!")
                
        elif opcao == "3":
            if agenda:
                nome = input("Digite o nome para buscar: ")
                if nome in agenda:
                    print(f"📞 {nome}: {agenda[nome]}")
                else:
                    print("❌ Contato não encontrado!")
            else:
                print("❌ Agenda vazia!")
                
        elif opcao == "4":
            if agenda:
                print("\n📒 AGENDA DE CONTATOS:")
                print("-" * 30)
                for nome, telefone in sorted(agenda.items()):
                    print(f"  {nome}: {telefone}")
                print("-" * 30)
                print(f"Total: {len(agenda)} contato(s)")
            else:
                print("📒 Agenda vazia!")
                
        elif opcao == "5":
            break
        else:
            print("❌ Opção inválida!")


def main():
    """Menu principal"""
    while True:
        print("\n" + "="*50)
        print(" 🐍 CÓDIGO DA TRANSFORMAÇÃO - PYTHON ")
        print("="*50)
        print("ATIVIDADES:")
        print("1. 🛒 Lista de Compras")
        print("2. 🎓 Dados do Aluno")
        print("3. 🔢 Pares e Ímpares")
        print("4. 📞 Agenda de Contatos (Extra)")
        print("5. 🚪 Sair")
        print("="*50)
        
        opcao = input("Escolha uma atividade (1-5): ")
        
        if opcao == "1":
            atividade1_lista_compras()
        elif opcao == "2":
            atividade2_dados_aluno()
        elif opcao == "3":
            atividade3_pares_impares()
        elif opcao == "4":
            atividade4_agenda()
        elif opcao == "5":
            print("\n✨ Programa encerrado! Até mais! ✨")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
