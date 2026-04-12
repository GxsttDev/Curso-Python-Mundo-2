Peso = int(input("Digite seu peso em KG: "))
Altura = float(input("Digite sua altura: "))
IMC = Peso / (Altura ** 2)

print (f"Seu IMC é: {IMC:.1f}")

if IMC < 18.5:
    print ("Você esta abaixo do peso ")
elif 18.5 <= IMC < 25:
    print ("Você esta no peso ideal ")
elif 25 <= IMC < 30:
    print ("Você esta acima do peso ")
elif 30 <= IMC < 40:
    print ("Você esta com obesidade ")
else:
    print ("Você esta com obesidade morbida, cuide da sua saude! ")