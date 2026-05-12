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

