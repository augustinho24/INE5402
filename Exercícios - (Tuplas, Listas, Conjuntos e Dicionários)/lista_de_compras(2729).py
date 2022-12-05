n = int(input())

while n != 0:
    n -= 1
    lista_compras = input().split()
    set_compras = set(lista_compras)
    lista_compras.clear()
    lista_compras.extend(set_compras)
    lista_compras.sort()

    print(*lista_compras)

    


    
