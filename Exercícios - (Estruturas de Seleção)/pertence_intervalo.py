#Verifcar um valor x(inteiro) pertence ao intervalo fechado [a,b].

#Entrada de dados:
pertence_intervalo = " "

x = int(input())
a = int(input())
b = int(input())


if (x >= a) and (x <= b): 
    pertence_intervalo = True
    print(pertence_intervalo)
    
else:
    pertence_intervalo = False
    print(pertence_intervalo)