y = int(input())

menor_valor = 0 

for c in range(0, y):
    x = int(input())
    if c == 0:
        menor_valor = x
    elif x < menor_valor:
        menor_valor = x
print(menor_valor)