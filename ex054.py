from datetime import date

AnoAtual = date.today().year
print (AnoAtual)
Maioridade = 0
Menoridade = 0
for pess in range(1,8):
   Nasc = int(input(f"Em que ano a {pess}ª pessoa nasceu: "))
   Idade = AnoAtual - Nasc
   if Idade >= 21:
      Maioridade += 1
   else:
      Menoridade += 1
print (f"Ao todo tivemos {Maioridade} pessoas maior de idade ")
print (f"E também tivemos {Menoridade} pessoas menor de idade ")