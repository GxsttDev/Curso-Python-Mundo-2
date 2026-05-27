N = int(input("Digite um número: "))
tot = 0
for c in range(1, N + 1):
    if N % c == 0:
        print(f"\033[34m{c} \033[0m", end="")
        tot += 1
    else:
        print(f"\033[31m{c} \033[0m", end="")
print (f"\nO número {N}, foi divisivel {tot} vezes\033[0m")
if tot == 2:
    print ("E por isso ele é PRIMO")
else:
    print ("E por isso ele NÃO É PRIMO")