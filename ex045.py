from random import randint

itens = ("Pedra", "Papel", "Tesoura")
Computador = randint(0, 2)
print ("""Suas Opcões 
[0] Pedra
[1] Papel
[2] Tesoura  """)
Jogador = int(input("Qual sua jogada: "))
print ("-=" * 12)
print (f"Computador jogou {itens[Computador]}")
print (f"Jogador jogou {itens[Jogador]}")
print ("-=" * 12)

if Computador == Jogador:
    print ("Resultado: EMPATE")
elif (Computador == "Tesoura" and Jogador == "Papel") or (Computador == "Pedra" and Jogador == "Tesoura") or (Computador == "Papel" and Jogador == "Pedra"):
    print ("Resultado: COMPUTADO VENCEU! ")
else:
    print("Resultado: JOGADOR VENCEDOR! ")