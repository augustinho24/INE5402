magico = True 

n = int(input())

M = []

for i in range(n):
    num = [int(x) for x in input().split()]
    M.append(num)

soma_diagonal_principal = 0
soma_diagonal_secundaria = 0


for i in range(n):
    for j in range(n):
        if i == j:
            soma_diagonal_principal += M[i][j]
        if i + j == n - 1:
            soma_diagonal_secundaria += M[i][j]

if soma_diagonal_principal != soma_diagonal_secundaria:
    magico = False

for j in range(n):
    soma_linha = 0
    soma_coluna = 0
    for i in range(n):
        soma_linha += M[i][j]
        soma_coluna += M[j][i]
    if soma_linha != soma_diagonal_principal or soma_coluna != soma_diagonal_principal:
        magico = False

print(magico)




