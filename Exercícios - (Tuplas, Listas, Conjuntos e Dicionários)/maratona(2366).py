while True:
    consegue = 'S'
    qtd_postos_agua, dist_intermediaria = [int(x) for x in input().split()]

    lista_postos_agua = [int(x) for x in input().split()]

    if len(lista_postos_agua) != qtd_postos_agua:
        break

    else:

        for p in range(len(lista_postos_agua) - 1):
            if (lista_postos_agua[p + 1] - lista_postos_agua[p]) > dist_intermediaria:
                consegue = 'N'
                break
            else:
                continue
    print(consegue)
    break

