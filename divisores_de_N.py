while True:
    N = int(input())
    if N == 0:
        break
    for i in range(1, N+1):
        if N % i == 0:
            print(f'{i}',end='  ')
        
