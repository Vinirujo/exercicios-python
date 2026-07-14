import random

# 🎯 Placar
pontos_jogador = 0
pontos_computador = 0

# 🎯 Opções possíveis
opcoes = ["pedra", "papel", "tesoura"]

while True:
    print("\n===== PEDRA PAPEL TESOURA =====")
    print("Placar:")
    print("Você:", pontos_jogador)
    print("Computador:", pontos_computador)
    print("\n1 - Jogar")
    print("0 - Sair")

    menu = input("Escolha: ")

    if menu == "1":

        jogador = input("Escolha pedra, papel ou tesoura: ").lower()
        computador = random.choice(opcoes)

        print("Computador escolheu: ", computador)

      

        if jogador == computador:
            print("Empate!")

        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            print("Você ganhou!")
            pontos_jogador += 1
        elif (computador == "pedra" and jogador == "tesoura") or \
             (computador == "papel" and jogador == "pedra") or \
             (computador == "tesoura" and jogador == "papel"):
             print("Computador ganhou!")
             pontos_computador += 1        
                                                         
    elif menu == "0":   
        print("Saindo do jogo...")
        break

    else:
        print("Opção inválida!")