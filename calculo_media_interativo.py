def media(n1,n2,n3,n4):
    media_final = (n1+n2+n3+n4)/4
    
    if media_final >= 7:
        return f"Sua media é {media_final :.1f} e você foi aprovado!"
    elif media_final >= 4:
        return f"Sua media é {media_final :.1f} e você está de recuperação!"
    else:
        return f"Sua media é {media_final :.1f} e você foi reprovado!"
    
n1 = float(input("Digite a primeira nota: "))   
n2 = float(input("Digite a segunda nota: "))   
n3 = float(input("Digite a terceira nota: "))   
n4 = float(input("Digite a quarta nota: "))   

print(media(n1,n2,n3,n4))