cont = 0

while True:
    cont += 1
    n = int(input())
    if n == 0: 
        break
    
    lista_participantes = [int(x) for x in input().split()]
    vencedor = [lista_participantes[x] for x in range(n) if lista_participantes[x] == x + 1]

    print(f" Teste {cont}")
    print(*vencedor)
    print()


