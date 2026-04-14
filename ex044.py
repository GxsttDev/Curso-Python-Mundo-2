print ("{:=^40}".format(" LOJA GUSTAVO "))
PrecoNormal = int(input("Digite o preço do produto: "))

print ("[1] Dinheiro ou Cheque: ")
print ("[2] A vista no Cartão ")
print ("[3] 2x no Cartão ")
print ("[4] 3x ou mais no Cartão ")
Pagamento = int(input("Qual sua opção: "))

if Pagamento == 1:
    PrecoFinal = PrecoNormal * 0.90
    print (f"Sua compra de {PrecoNormal}, vai custar {PrecoFinal:.2f}")
elif Pagamento == 2:
    PrecoFinal = PrecoNormal * 0.95
    print (f"Sua compra de {PrecoNormal}, vai custar {PrecoFinal:.2f}")
elif Pagamento == 3:
    Parcela = PrecoNormal / 2 
    print (f"Sua compra sera parcelada em 2x de R${Parcela:.2f}, total de R${PrecoNormal}")
elif Pagamento == 4:
    PrecoFinal = PrecoNormal * 1.20
    TotParcela = int(input("Quantas parcelas? "))
    Parcela = PrecoFinal / TotParcela
    print (f"Sua conta sera parcelada em {TotParcela}x de R${Parcela:.2f} com JUROS")
    print (f"Sua compra de R${PrecoNormal}, vai custar R${PrecoFinal:.2f}")
    
print ("{:=^40}".format(" OBRIGADO, VOLTE SEMPRE! "))