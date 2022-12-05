O = input()

soma = 0
cont = 0
M = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    M.append(linha)

for i in range(12):
    for j in range(0,i):
            soma += M[i][j]
            cont += 1

if O == 'S':
    print(soma)
elif O == 'M':
    media= soma/cont
    print(f'{media:.1f}')

