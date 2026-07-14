def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        return "Não é possivel dividir por zero."
    return a / b

while True:
    print("==== MENU ====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo numero: "))
        print(f"A soma é: {soma(a,b)}")
        
    elif opcao == 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo numero: "))
        print(f"A subtração é: {subtracao(a,b)}")

    elif opcao == 3:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo numero: "))
        print(f"A multiplicação é: {multiplicacao(a,b)}")
        
    elif opcao == 4:
        a = float(input("Digite o primeiro número: ")) 
        b = float(input("Digite o segundo número: "))
        print(f"A divisão é: {divisao(a,b)}")
        
    elif opcao == 0:
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")    
















    
        
        
        
        
        