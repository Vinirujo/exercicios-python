def verificar_numero(num):
    if num %2 == 0:
        return "Um numero Par"
    else:
        return "Um numero Impar"
    
num = int(input("Digite um numero: "))
resultado = verificar_numero(num)

print(f"O número {num} é {resultado}")