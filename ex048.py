Soma = 0
Cont = 0
for c in range(1, 501, 2):
    if c % 2 != 0 and c % 3 == 0:
        Soma = Soma + c
        Cont = Cont + 1
print (f"O total de valores solicitados é: {Cont}, e a soma entre todos eles é: {Soma}")