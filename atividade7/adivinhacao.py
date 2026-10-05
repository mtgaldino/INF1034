import random

def modo_usuario_adivinha():
    numero_secreto = random.randint(1, 1023)
    tentativas = 0
    acertou = False
    
    print("\n--- MODO: Você adivinha ---")
    print("Pensei em um número entre 1 e 1023. Tente adivinhar!")
    
    while not acertou:
        chute = int(input("Seu chute: "))
        tentativas += 1
        
        if numero_secreto < chute:
            print("-1 (O número secreto é MENOR)")
        elif numero_secreto > chute:
            print("1 (O número secreto é MAIOR)")
        else:
            print("0 (ACERTOU!)")
            print(f"Você acertou em {tentativas} tentativas!")
            acertou = True

def modo_computador_adivinha():
    print("\n--- MODO: Computador adivinha ---")
    print("Pense em um número entre 1 e 1023, mas não me conte!")
    input("Pressione ENTER quando estiver pronto...")
    
    inicio = 1
    fim = 1023
    tentativas = 0
    acertou = False
    
    while not acertou and inicio <= fim:
        chute_pc = (inicio + fim) // 2
        tentativas += 1
        
        print(f"\nMeu chute é: {chute_pc}")
        print("Responda:")
        print(" -1 : Se o seu número for MENOR")
        print("  1 : Se o seu número for MAIOR")
        print("  0 : Se eu ACERTEI")
        
        resposta = int(input("Sua resposta (-1, 1 ou 0): "))
        
        if resposta == -1:
            fim = chute_pc - 1
        elif resposta == 1:
            inicio = chute_pc + 1
        elif resposta == 0:
            print(f"Eu (computador) acertei em apenas {tentativas} tentativas!")
            acertou = True
        else:
            print("Resposta inválida! Por favor, responda apenas -1, 1 ou 0.")

def menu_adivinhacao():
    rodando = True
    while rodando:
        print("\n=== JOGO DE ADIVINHAÇÃO (1 a 1023) ===")
        print("1. Eu quero adivinhar o número do computador")
        print("2. Quero que o computador adivinhe meu número")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1-3): ").strip()
        
        if opcao == '1':
            modo_usuario_adivinha()
        elif opcao == '2':
            modo_computador_adivinha()
        elif opcao == '3':
            print("Saindo do jogo...")
            rodando = False
        else:
            print("Opção inválida!")


menu_adivinhacao()