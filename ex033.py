N1 = int(input("Digite o PRIMEIRO número: "))
N2 = int(input("Digite o SEGUNDO número: "))
N3 = int(input("Digite o TERCEIRO número: "))

MaiorNumero = N1
MenorNumero = N1

if N2 > MaiorNumero: 
    MaiorNumero = N2
if N2 < MenorNumero:
    MenorNumero = N2
if N3 > MaiorNumero:
    MaiorNumero = N3
if N3 < MenorNumero:
    MenorNumero = N3

print (f"O maior numero é {MaiorNumero}")
print (f"O menor numero é {MenorNumero}")