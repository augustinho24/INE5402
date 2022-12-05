a=int(input())
b=int(input())

contador = 0


if a < b:
    for cu in range (a, b+1):
        contador +=1
        if cu == b:
            print(contador)

elif a > b:
    
    for cu in range (b, a+1):
        contador +=1
        if cu == a:
            print(contador)

elif a == b:
    contador +=1
    print(contador)
            


