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

