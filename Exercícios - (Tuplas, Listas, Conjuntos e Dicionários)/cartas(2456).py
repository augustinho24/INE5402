cartas = [int(x) for x in input().split()]

c2 = cartas.copy()
c2.sort()

c3 = cartas.copy()
c3.sort()
c3.reverse()

ver_org = 'C'
if c2 == cartas and len(cartas) <= 13:

    for i in range(len(cartas)-1):
        if cartas[i+1] < cartas[i]: 
            ver_org = 'N'
        
elif c3 == cartas and len(cartas) <= 13:
    
    for i in range(0,len(cartas)-1):
        if cartas[i+1] > cartas[i]: 
            ver_org = 'N'
        else:
            ver_org = 'D'

else:
    ver_org = 'N'

    
print(ver_org)
