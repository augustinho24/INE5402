n = int(input())
m = int(input())
cont = 0
for u in range (m+1):
    cont += 1
    if cont % n == 0:
        i = cont
        print(i, end=' ')

if m == 0:
    print('mad sus')
