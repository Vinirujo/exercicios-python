import random


def ler_int(prompt: str, minimo: int = 1, maximo: int = 100):
    """Lê um inteiro do usuário entre `minimo` e `maximo`.
    Retorna None se o usuário digitar 'sair'."""
    while True:
        texto = input(prompt).strip()
        if texto.lower() in ("sair", "exit", "q"):
            return None
        try:
            valor = int(texto)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'sair' para encerrar.")
            continue
        if valor < minimo or valor > maximo:
            print(f"Digite um número entre {minimo} e {maximo}.")
            continue
        return valor


def jogar():
    print("Bem-vindo ao jogo da Adivinhação!")
    print("Vou pensar em um número entre 1 e 100.")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        chute = ler_int("Tente adivinhar o número (ou digite 'sair' para encerrar): ")
        if chute is None:
            print("Jogo encerrado pelo usuário.")
            return
        tentativas += 1
        print("\n====================")

        if numero_secreto < chute:
            print("Tente um número menor.")
        elif numero_secreto > chute:
            print("Tente um número maior.")
        else:
            print("Você acertou!")
            if tentativas == 1:
                print("Você acertou de primeira! Parabéns!")
            else:
                print(f"Você acertou com {tentativas} tentativas.")
            break


def main():
    while True:
        jogar()
        resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if resposta not in ("s", "sim"):
            print("Obrigado por jogar! Até a próxima.")
            break


if __name__ == "__main__":
    main()


