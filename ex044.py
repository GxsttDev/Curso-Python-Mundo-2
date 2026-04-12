PrecoNormal = int(input("Digite o preço do produto: "))
print ("===== LOJA DO GUSTAVO =====")
print ("[1] Dinheiro ou Cheque: ")
print ("[2] A vista no Cartão ")
print ("[3] 2x no Cartão ")
print ("[4] 3x ou mais no Cartão ")
Pagamento = int(input("Qual sua opção: "))

if Pagamento == 1:
    PrecoFinal = PrecoNormal * 0.90
    print (f"Sua compra de {PrecoNormal}, vai custar {PrecoFinal}")
elif Pagamento == 2:
    PrecoFinal = PrecoNormal * 0.95
    print (f"Sua compra de {PrecoNormal}, vai custar {PrecoFinal}")
elif Pagamento == 3:
    print (f"Sua compra vai custar: {PrecoNormal}")
elif Pagamento == 4:
    PrecoFinal = PrecoNormal * 1.20
    print (f"Com o juros da parcela sua compra custara: {PrecoFinal}")

print ("===== OBRIGADO, VOLTE SEMPRE =====")