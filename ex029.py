Velocidade = int(input("Qual velocidade seu carro estava: "))

if Velocidade > 80:
    Excesso = Velocidade - 80
    Multa = Excesso * 7
    print ("Você foi MULTADO!")
    print (f"Excesso: {Excesso} Km/h")
    print (f"Valor da multa: R${Multa:.2f}")
else:
    print ("Você NÃO foi multado")