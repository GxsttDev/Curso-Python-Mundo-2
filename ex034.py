Salario = int(input("Digite o valor do salario: R$"))

if Salario > 1250:
    Aumento = 1.10
    Salario = Salario * Aumento
else:
    Aumento = 1.15
    Salario = Salario * Aumento
print (f"O salario com aumento fica: R${Salario:.2f}")