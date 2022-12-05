#Maior de uma sequência e sua posição

maior_valor = 0
pos = 0

r = int(input())

for i in range (1, r+1):
    x = int(input())
    
    if i == 0:
        maior_valor = 0
    elif x > maior_valor:
        pos = i
        maior_valor = x
    
    

print(maior_valor,pos)