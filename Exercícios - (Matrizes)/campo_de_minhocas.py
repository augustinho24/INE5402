minhocas_colhidas = 0

N, M = [int(cu) for cu in input().split()]
celulas = []
prod_maior = 0

for i in range(N):
    minhocas = [int(x) for x in input().split()]
    celulas.append(minhocas)

#verificar a maior producao por linha

for i in range(N):
    prod_linha = 0
    prod_linha = sum(celulas[i])
    if prod_linha > prod_maior:
        prod_maior = prod_linha

#verificar a maior producao por coluna

for i in range(M):
    prod_coluna = 0
    for j in range(N):
        prod_coluna += celulas[j][i]
    if prod_coluna > prod_maior:
        prod_maior = prod_coluna

print(prod_maior)

