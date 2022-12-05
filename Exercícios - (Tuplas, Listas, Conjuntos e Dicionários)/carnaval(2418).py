import math
notas = [float(x) for x in input().split()]
menor_nota = math.inf
pos_menor_nota = 0
maior_nota = -math.inf
pos_maior_nota = 0
for i in range(len(notas)):

    if notas[i] > maior_nota:

        maior_nota = notas[i]
        pos_maior_nota = i
    
    if notas[i] < menor_nota:
        menor_nota = notas[i]
        pos_menor_nota = i


notas.pop(pos_maior_nota)
notas.pop(pos_menor_nota)
soma_notas = sum(notas)

print(f"{soma_notas:.1f}")