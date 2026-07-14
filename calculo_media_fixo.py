def media (n1,n2,n3,n4):
    return (n1+n2+n3+n4)/4

resultado = media(10,6.5,4,9) 

print(f"Média: {resultado:.1f}")   

if resultado >= 7:
    print("Aprovado")
elif resultado >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    
