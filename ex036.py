ValorCasa = float(input("Qual o valor da casa: R$"))
Salario = float(input("Qual o seu salario: R$ "))
Anos = int(input("Em quantos anos você vai pagar: "))
Prestacoes = ValorCasa / (Anos * 12)

if Prestacoes <= Salario * 0.30:
    print ("STATUS DO EMPRESTIMO: [AUTORIZADO]")
elif Prestacoes > Salario * 0.30:
    print ("STATUS DO EMPRESTIMO: [NÃO AUTORIZADO]")