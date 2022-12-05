p0 = int(input())
p1 = int(input())
p2 = int(input())

acumula_data_comemorativa = 0

if p0 != p1:
    acumula_data_comemorativa += 1 

if p0 != p2:
    acumula_data_comemorativa += 1

if p1 != p2:
    acumula_data_comemorativa += 1

if p1 == p2 and p0 == p1:
    acumula_data_comemorativa = 1

print(acumula_data_comemorativa)