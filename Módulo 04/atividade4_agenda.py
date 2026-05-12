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