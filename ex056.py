somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
mulherabaixo = 0

for p in range(1,5):
    print (f" ----- {p}ª PESSOA ----- ")
    nome = str(input("NOME: ")).strip()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        mulherabaixo += 1

mediaidade = somaidade / 4
print (f"A média de idade do grupo é de {mediaidade} anos ")
print (f"O homem mais velho tem: {maioridadehomem} e se chama: {nomevelho}")
print (f"O total de mulheres abaixo de 20 anos é: {mulherabaixo}")