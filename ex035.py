Reta1 = int(input("Digite o comprimento da primeira reta: "))
Reta2 = int(input("Digite o comprimento da segunda reta: "))
Reta3 = int(input("Digite o comprimento da terceira reta: "))

if (Reta1 + Reta2) > Reta3 and (Reta1 + Reta3) > Reta2 and (Reta2 + Reta3) > Reta1:
    print ("PODE formar um Triangulo! ")
else:
    print ("NÃO pode formar um triangulo. ")