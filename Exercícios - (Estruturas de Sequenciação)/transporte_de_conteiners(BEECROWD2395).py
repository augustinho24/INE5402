#Transporte de contêineres - BEECROWD2395

a,b,c = [int(cu) for cu in input().split()]
x,y,z = [int(cu) for cu in input().split()]

capacidade = (x//a) * (y//b) * (z//c)
print(capacidade)

