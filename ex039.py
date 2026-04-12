from datetime import date

AnoNasc = int(input("Digite o ano em que você nasceu: "))
AnoAtual = date.today().year
Idade =  AnoAtual - AnoNasc
AnoAlistamento  = AnoNasc + 18

if Idade == 18:
    print ("Está na hora de você se alistar! ")
elif Idade < 18:
    FaltaAnos = 18 - Idade
    print (f"Ainda Falta {FaltaAnos} anos para você se alistar, você ira se alistar em:  {AnoAlistamento}")
else:
    print (f"O seu ano de alistamento já passou, ele era em: {AnoAlistamento}")
