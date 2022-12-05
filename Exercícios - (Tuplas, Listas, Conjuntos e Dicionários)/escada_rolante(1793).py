while True:
    contagem = 10

    N = int(input())
    if N == 0:
        break

    T = [int(x) for x in input().split()]
    
    if len(T) == 1:
        print(contagem)
        
    else:
        for i in range(0,len(T)-1):
            if abs(T[i]-T[i+1]) <= 10:
                contagem += abs(T[i]-T[i+1])
            else:
                contagem += 10
                
        print(contagem)


