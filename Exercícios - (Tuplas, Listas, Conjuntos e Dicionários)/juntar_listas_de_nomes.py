lista_1 = []
lista_2 = []
lista_3 = []

n1 = int(input("Quantidade de nomes na Lista 1: "))
while n1 > 0:
    n1 -= 1 
    lista_1.append(input())

n2 = int(input("Quantidade de nomes na Lista 2: "))
while n2 > 0:
    n2 -= 1
    lista_2.append(input())

lista_3 = lista_1 + lista_2
lista_3.sort()

print(*lista_3, sep= '\n')



