def media_geo(n):
    produto = 1
    lista = []
    for _ in range(1,n+1):
        lista.append(float(input()))    
    for valor in lista:
        produto *= valor 
       
    media = produto ** (1/n) 
    return media

x = int(input())

print(media_geo(x))
    



