O = input()

soma = 0
cont = 0
lin = 12
M = []

for i in range(12):
    lin -= 1
    linha = []
    for j in range(12):
        linha.append(float(input()))
        if j < lin:
            soma += linha[j]
            cont += 1
            M.append(linha)



if O == 'S':
    print(soma)
elif O == 'M':
    media= soma/cont
    print(f'{media:.1f}')



