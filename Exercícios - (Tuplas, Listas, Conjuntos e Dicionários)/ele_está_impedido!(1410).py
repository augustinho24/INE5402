while True:
    
    A, D = [int(x) for x in input().split()]
    if not (A or D):
        break
    
    pos_A = [int(x) for x in input().split()]
    pos_D = [int(x) for x in input().split()]
    
    pos_A.sort()
    pos_D.sort()

    if pos_A[0] >= pos_D[1]:
        print('N')
    else:
        print('Y')
    
           




           


