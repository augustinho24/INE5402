#Cálculo de salário líquido	

#Entrada de dados:

horas_trabalhadas = int(input())
horas_extras = int(input())
salario_bruto = round((12.50*horas_trabalhadas)+(15.00*horas_extras),2)
ir = round((salario_bruto*0.13),2)
inss = round((salario_bruto*0.09),2)

salario_liquido = salario_bruto - (ir+inss)

print(f"- Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (13%) : R$ {ir:.2f}")
print(f"- INSS (9%) : R$ {inss:.2f}")
print(f"- Salário Líquido : R$ {salario_liquido:.2f}")