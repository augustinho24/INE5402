import math

n = int(input())

if n == 1:
    verifica_primo = False
elif n != 2 and n % 2 == 0:
    verifica_primo = False
else:
    verifica_primo = True
    raiz = int(math.sqrt(n))
    for i in range(3, raiz+1, 2):
        if n % i == 0:
            verifica_primo = False
            break
    
print(verifica_primo)    