#Calcular a porção de mandioca do Curipira, Boitatá, Boto, Mapinguari e Iara, mais a porção fixa da Dona Chica, que é 225 gramas.

# Entrada mais simples:
# Cu, Tata, Boto, Mapi, Iara = [int(x) for x in input().split()]

Cu = int(input())
Tata = int(input())
Boto = int(input())
Mapi = int(input())
Iara = int(input())

mandioca = ((300*Cu) + (1500*Tata) + (600*Boto) + (1000*Mapi) + (150*Iara) + 225)

print(mandioca)