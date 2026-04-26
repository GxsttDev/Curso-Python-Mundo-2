print ("="*23)
print ("10 TERMOS DE UMA PA: ")
print ("="*23)

Termo1 = int(input("Primeiro Termo: "))
Razao = int(input("Razão: "))
Decimo = Termo1 + (10 - 1) * Razao
for c in range(Termo1,Decimo + Razao,Razao):
    print (f"{c} ",end="→ ")
print ("ACABOU")