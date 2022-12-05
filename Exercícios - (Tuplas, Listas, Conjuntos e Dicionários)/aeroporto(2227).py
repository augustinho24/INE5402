contador = 0

while True:
    contador += 1

    A, V = [int(x) for x in input().split()]

    lista_aeroportos = [0] * A

    if A == 0 and V == 0:
        break

    for i in range(V):
        X, Y = [int(x) for x in input().split()]
        lista_aeroportos[X-1] += 1
        lista_aeroportos[Y-1] += 1
    
    print(f'Teste {contador}')

    aeroportos_com_maior_trafego = []

    for i in range(A):
        if lista_aeroportos[i] == max(lista_aeroportos):
            aeroportos_com_maior_trafego.append(i+1)

    print("{0} \n".format(" ".join(list(map(str,aeroportos_com_maior_trafego)))))
    
    #for i in aeroportos_com_maior_trafego:
        #print(i, end=' ')


