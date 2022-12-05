#Cálculo de energia elétrica

custo = 0
kwh_recebe = int(input("Kwh consumidos: "))
kwh = float(kwh_recebe)

if kwh <= 30.00:
    custo = (kwh * 0.09556)
    x = round(custo,2)
    print(f"{x:.2f}")

elif kwh > 30.00 and kwh <= 100.00:
    custo = ((30 * 0.09556) + ((kwh - 30) * 0.16698))
    x = round(custo,2)
    print(f"{x:.2f}")

elif kwh > 100 and kwh <= 200:
    custo = (((30 * 0.09556) + (70 * 0.16698) + ((kwh - 100) * 0.25052)))
    x = round(custo,2)
    print(f"{x:.2f}")
else:
    custo = (((30 * 0.09556) + (70 * 0.16698) + (100 * 0.25052) + ((kwh - 200) * 0.27836)))
    x = round(custo,2)
    print(f"{x:.2f}")


