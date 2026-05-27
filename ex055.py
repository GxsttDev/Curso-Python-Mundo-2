MaiorPeso = 0
MenorPeso = 0
for pess in range(1,6):
    Peso = float(input(f"Digite o peso da {pess}ª pessoa: "))
    if pess == 1:
        MaiorPeso = Peso
        MenorPeso = Peso
    else:
        if Peso > MaiorPeso:
            MaiorPeso = Peso
        if Peso < MenorPeso:
            MenorPeso = Peso
print (f"O maior peso digitado foi de {MaiorPeso}Kg")
print (f"O menor peso digitado foi de {MenorPeso}Kg")