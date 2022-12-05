def fibo(x):
    x = int(x)
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:


        a = 1
        b = 1
        for i in range(3 , x+1):
            c = a + b
            a = b
            b = c
        return c

n = int(input())
print(fibo(n))