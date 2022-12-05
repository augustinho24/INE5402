import math

n0 = int(input())
n1 = int(input())
qtd_primos = 0 

for u in range (n0, n1+1):
    if u == 1:
        verifica_primo = False
    elif u != 2 and u % 2 == 0:
        verifica_primo = False
    else:
        verifica_primo = True
        qtd_primos += 1
        raiz = int(math.sqrt(u))
        for i in range(3, raiz+1, 2):
            if u % i == 0:
                verifica_primo = False
                qtd_primos -= 1

print(qtd_primos)