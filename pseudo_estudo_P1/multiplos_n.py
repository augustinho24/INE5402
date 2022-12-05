n = int(input())
m = int(input())
cont = 0
for u in range (m+1):
    cont += 1
    if cont % n == 0:
        multiplos = cont
        print(multiplos, end='  ')

