from datetime import date

AnoNasc = int(input("Digite em qual ano você nasceu: "))
AnoAtual = date.today().year
Idade = AnoAtual - AnoNasc

if Idade <= 9:
    print ("Sua categoria é: MIRIM")
elif Idade > 9 and Idade <= 14:
    print ("Sua categoria é: INFANTIL")
elif Idade > 14 and Idade <= 19:
    print ("Sua categoria é: JUNIOR")
elif Idade > 19 <= 20:
    print ("Sua categoria é: SÊNIOR")
else:
    