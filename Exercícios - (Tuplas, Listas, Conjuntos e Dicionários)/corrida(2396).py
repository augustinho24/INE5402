
primeiro = 0

segundo = 0

terceiro = 0

qtd_carros, voltas = [int(x) for x in input().split()]

carros = []

for carro in range(qtd_carros):
    carros.append(sum([int(x) for x in input().split()]))
    
copia_carros = carros.copy()
copia_carros.sort()


for c in range(len(carros)):
    if carros[c] == copia_carros[0]:
        primeiro = c+1
    elif carros[c] == copia_carros[1]:
        segundo = c+1
    elif carros[c] == copia_carros[2]:
        terceiro = c+1


print(primeiro)

print(segundo)

print(terceiro)