Reta1 = int(input("Digite o comprimento da primeira reta: "))
Reta2 = int(input("Digite o comprimento da segunda reta: "))
Reta3 = int(input("Digite o comprimento da terceira reta: "))

if (Reta1 + Reta2) > Reta3 and (Reta1 + Reta3) > Reta2 and (Reta2 + Reta3) > Reta1:
    print ("PODE formar um Triangulo! ")
    if Reta1 == Reta2 == Reta3:
        print ("Esse triangulo é: EQUILATERO")
    elif Reta1 == Reta2 or Reta1 == Reta3 or Reta2 == Reta3:
        print ("Esse triangulo é: ISOCELES")
    else:
        print ("Esse triangulo é: ESCALENO")
else:
    print ("NÃO pode formar um triangulo. ")