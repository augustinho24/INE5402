#Desvio padrão
import math
def desvio_padrao(x):
    lista = [] 
    for _ in range(1,x+1):
        lista.append(float(input()))
    media = sum(lista) / x
    soma = 0
    for valor in lista:
        soma += (valor - media) ** 2
    desvio = math.sqrt((soma / (x-1)))
    return desvio

z = int(input())

print(f"{(desvio_padrao(z)):.8f}")

    








