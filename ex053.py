Frase = str(input("Digite uma frase: ")).strip().upper()
Palavra = Frase.split()
Junto = "".join(Palavra)
Inverso = Junto[::-1]
print (f"O inverso de: {Junto} é: {Inverso}")
if Inverso == Junto:
    print ("A frase digitada é um PALÍNDROMO! ")
else:
    print ("A frase digitada NÃO É UM PALINDROMO! ")