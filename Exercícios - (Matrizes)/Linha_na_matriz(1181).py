L = int(input())
T = input().upper()

M = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    M.append(linha)

soma = 0
soma += sum(M[L])


if T == 'S':
    print(soma)
elif T == 'M':
    print(f"{soma/12:.1f}")


