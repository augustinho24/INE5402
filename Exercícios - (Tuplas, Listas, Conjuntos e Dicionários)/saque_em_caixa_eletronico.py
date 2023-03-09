#Saque de valor em Caixa Eletrônico


cedulas = {}
cedulas_sacar = {}
list_qtd_cedulas = []
quantidade_cedulas_sacar = 0
valor_cedula = 0

n = int(input())

for _ in range (n):
    valor_cedula = float(input('Valor da cédula: '))
    quantidade_cedulas = int(input('Quantidade de cédulas: '))
    cedulas[valor_cedula] = quantidade_cedulas


valor_saque = float(input())

for valor_cedula in sorted(cedulas.keys(), reverse=True):
    quantidade_cedulas = cedulas[valor_cedula]
    
    while valor_saque >= valor_cedula and quantidade_cedulas > 0:
        valor_saque -= valor_cedula
        quantidade_cedulas -= 1
        quantidade_cedulas_sacar += 1
        
    if quantidade_cedulas_sacar >= 0:
        cedulas_sacar[valor_cedula] = quantidade_cedulas_sacar
        quantidade_cedulas_sacar = 0

if valor_saque == 0:
    for valor_cedula in sorted(cedulas_sacar.keys(), reverse=True):
        quantidade_cedulas = cedulas_sacar[valor_cedula]
        list_qtd_cedulas.append(quantidade_cedulas)



print(*list_qtd_cedulas[::-1])
    






    