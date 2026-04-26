Distancia = int(input("Qual a distancia da viagem em KM: "))

if Distancia > 200:
    Passagem = Distancia * 0.45
else:
    Passagem = Distancia * 0.50
print (f"O preço da passagem é: R${Passagem:.2f}")