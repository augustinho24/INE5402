def fat(x):
    if x == 0:
        return 1
    else:
        return x * fat (x-1)

n = int(input())
print(fat(n))