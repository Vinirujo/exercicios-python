numero = []

while True:
    print("------------   MENU    ------------")
    print("1. Adicionar número")
    print("2. Remover número")
    print("3. Listar números")
    print("4. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if opcao == 1:
        try:
            num = int(input("Digite um número para adicionar: "))
            numero.append(num)
            print(f"Número {num} adicionado com sucesso!")
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opcao == 2:
        try:
            num = int(input("Digite um número para remover: "))
            if num in numero:
                numero.remove(num)
                print(f"Número {num} removido com sucesso!")
            else:
                print("Número não encontrado na lista.")
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opcao == 3:
        if numero:
            print("Números na lista:")
            for num in numero:
                print(num)
        else:
            print("A lista está vazia.")

    elif opcao == 4:
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Escolha entre 1 e 4.")
