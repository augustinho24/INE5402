ver_compatibilidade = 'N'

conectores_x = [int(x) for x in input().split()]

conectores_y = [int(x) for x in input().split()]

conector_compativel_x = []

for conector in range(len(conectores_x)):

    if conectores_x[conector] == 1:
        conector_compativel_x.append(0)
    else:
        conector_compativel_x.append(1)

if conectores_y == conector_compativel_x:
    ver_compatibilidade = 'Y'

print(ver_compatibilidade)
    
