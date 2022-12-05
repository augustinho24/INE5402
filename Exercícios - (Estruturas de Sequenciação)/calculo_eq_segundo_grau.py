#Calculo de raizesz de uma funçao quadratica

import math

a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))
c = int(input("Digite um valor para c: "))

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta)) / (2*a)

x2 = (-b - math.sqrt(delta)) / (2*a)

print("As raizes reais sao: ", x1, "e:", x2)