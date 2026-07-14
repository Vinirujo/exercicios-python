# Entrada
numero = int(input("Digite um número de 4 dígitos: "))

# Processamento
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000

invertido = (unidade * 1000) + (dezena * 100) + (centena * 10) + milhar

# Saída
print("Número invertido:", invertido)