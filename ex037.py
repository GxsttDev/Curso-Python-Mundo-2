numero = int(input("Digite um numero inteiro: "))
print ("Escolha a base de conversão: ")
print ("[1] BINARIO ")
print ("[2] OCTAL ")
print ("[3] HEXADECIMAL ")
opcao = int(input("QUAL SUA OPÇÃO: "))

if opcao == 1:
    print (f"{numero} em binario é igual a: {bin(numero)}")
elif opcao == 2:
    print (f"{numero} em octal é igual a: {oct(numero)}")
elif opcao == 3: 
    print (f"{numero} em hexadecimal é igual a: {hex(numero)}")
else:
    print (f"OPÇÃO INVALIDA, escolha [1] , [2] ou [3]")