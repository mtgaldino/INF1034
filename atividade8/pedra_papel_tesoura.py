import random

def obter_escolha_computador():
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    
    # Condições em que o jogador ganha
    if (jogador == "pedra" and computador == "tesoura") or \
       (jogador == "tesoura" and computador == "papel") or \
       (jogador == "papel" and computador == "pedra"):
        return "jogador"
    else:
        return "computador"

def jogar_pedra_papel_tesoura():
    placar_jogador = 0
    placar_computador = 0
    
    print("=== BEM-VINDO AO PEDRA, PAPEL E TESOURA ===")
    
    jogando = True
    while jogando:
        print(f"\nPlacar: Você {placar_jogador} x {placar_computador} Computador")
        
        # Leitura e validação simples
        escolha_usuario = input("Escolha (pedra, papel, tesoura): ").strip().lower()
        if escolha_usuario not in ["pedra", "papel", "tesoura"]:
            print("Opção inválida! Tente novamente.")
            continue
            
        escolha_comp = obter_escolha_computador()
        print(f"O computador escolheu: {escolha_comp}")
        
        resultado = determinar_vencedor(escolha_usuario, escolha_comp)
        
        if resultado == "empate":
            print("Empate nesta rodada!")
        elif resultado == "jogador":
            print("Você venceu esta rodada!")
            placar_jogador += 1
        else:
            print("O computador venceu esta rodada!")
            placar_computador += 1
            
        resposta = input("\nDeseja jogar outra rodada? (s/n): ").strip().lower()
        if resposta != 's':
            jogando = False
            
    print(f"\nJogo encerrado! Placar final: Você {placar_jogador} x {placar_computador} Computador")


jogar_pedra_papel_tesoura()