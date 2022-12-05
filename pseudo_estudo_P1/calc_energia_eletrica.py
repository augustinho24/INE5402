kwh = float(input())
tarifa = 0

if kwh <= 30:
    tarifa = kwh * 0.09556
elif kwh <= 100:
    tarifa = (30 * 0.09556) + ((kwh - 30)*0.16698)
elif kwh <= 200:
    tarifa = (30 * 0.09556) + (70*0.16698) + ((kwh - 100) * 0.25052)
else:
    tarifa = (30 * 0.09556) + (70*0.16698) + (100 * 0.25052) + ((kwh - 200) * 0.27836)
    
print(f"{tarifa:.2f}")





