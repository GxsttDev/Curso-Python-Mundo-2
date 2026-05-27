Cont = 0
Soma = 0
for c in range(1,7):
    Cont = Cont + 1
    N = int(input(f"Digite o {Cont}o numero: "))
    if N % 2 == 0:
        Soma = Soma + N
print (f"A soma dos números pares é: {Soma}")