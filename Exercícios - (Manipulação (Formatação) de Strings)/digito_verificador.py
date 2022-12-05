numero = input()

soma = 0
peso = len(numero)
for i in range(len(numero) - 1):
    
    soma += int(numero[i]) * peso
    peso -= 1
dv = 11 - soma % 11
if dv >= 10:
    dv = 0

print(dv == int(numero[-1]))