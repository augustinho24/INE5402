while True:
    m = []
    t = int(input())

    if t == 0: break

    for i in range(0,t):
        linha = 2**i
        m.append(linha)
        if i > 1:
            for j in range(0,i):
                linha = linha*2
                m.append(linha)

        

    print(m)