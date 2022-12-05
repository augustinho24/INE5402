salario_bruto = float(input())

if salario_bruto <= 720.00:
    inss = salario_bruto * 0.0765
    print(f"{inss:.2f}")

elif salario_bruto <= 1200.00:
    inss = salario_bruto * 0.09
    print(f"{inss:.2f}")

elif salario_bruto <= 2400.00:
    inss = salario_bruto * 0.11
    print(f"{inss:.2f}")

elif salario_bruto > 2400.00:
    inss = 2400.00 * 0.11
    print(f"{inss:.2f}")