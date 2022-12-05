#Jogo de varetas 

while True:
    retangulos = 0
    soma_varetas = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        comprimento, varetas = [int(x) for x in input().split()]
        if varetas % 2 != 0:
            varetas -= 1
            soma_varetas += varetas
        else:
            soma_varetas += varetas
    retangulos = soma_varetas // 4
    print(retangulos)

