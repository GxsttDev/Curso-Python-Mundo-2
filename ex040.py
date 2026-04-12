Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
Media = (Nota1 + Nota2) / 2 

print (f"Sua média foi: {Media:.1f}")

if Media < 5:
    print ("Você foi REPROVADO!")
elif Media > 5 and Media < 6.9:
    print ("Você está de RECUPERAÇÃO!")
else:
    print ("Você foi APROVADO!")