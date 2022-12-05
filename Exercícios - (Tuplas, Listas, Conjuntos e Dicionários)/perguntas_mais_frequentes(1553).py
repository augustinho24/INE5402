while True:
    N , K = [int(x) for x in input().split()]
    if N == 0 or K == 0:
        break
    pergunta_frequente = 0
    P = [int(x) for x in input().split()]
    P.sort()
    setP = set(P)
    listaP = list(setP)
    listaP.sort()

    for i in range(len(listaP)):
        if P.count(listaP[i]) >= K:
            pergunta_frequente = listaP[i]
    print(pergunta_frequente)

