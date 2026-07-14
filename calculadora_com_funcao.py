def calculadora(n1,n2,op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Divisão por zero"
    else:
        return "operação inválida"
    
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

resultado = calculadora(n1,n2,op)
print(f"Resultado: {resultado}")