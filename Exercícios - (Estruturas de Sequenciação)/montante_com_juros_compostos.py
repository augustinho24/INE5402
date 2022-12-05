#Cálculo de montante com juros compostos

import math

c=float(input("Digite o valor do capital investido: "))
t=int(input("Dígite a quantidade de meses: ")) 
i=float(input("Dígite o valor da porcentagem da taxa de juros: "))

montante = round(c*(1+i/100)**t,2)


print(f"{montante:.2f}")

