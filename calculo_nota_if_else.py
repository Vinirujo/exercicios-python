nota1=float(input("Digite sua nota:"))
nota2=float(input("Digite sua seguda nota:"))
media=(nota1+nota2)/2

if media >= 5:
    print("aprovado")

elif media >= 3 and  media <= 5:
    print("enxame")

else:
    print("reprovado")