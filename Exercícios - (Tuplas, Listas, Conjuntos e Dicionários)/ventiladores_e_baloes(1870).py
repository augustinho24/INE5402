while True:
    L, C, P = [int(x) for x in input().split()]
    if  L == 0 or C == 0 or P == 0:
        break

    boom = False
    P -= 1

    for k in range(L):

        linha = [int(x) for x in input().split()] 
        
        if not boom:
            u = P
            while linha[u] == 0:
                u -= 1
            v = P
            while linha[v] == 0:
                v += 1
                
            P = P - linha[v] + linha[u]
            if P <= u or P >= v:
                boom = True
                P = max(min(v, P), u)
                linha_boom = k

    P += 1
    if boom:
        linha_boom += 1
        print(f"BOOM {linha_boom} {P}")
    else:
        print(f"OUT {P}")
    