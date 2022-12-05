import math

# Entrada de dados:

m2=int(input())
m2_por_litro=m2 / 18
num_galao= max(round(m2_por_litro/ 3.6),1)
valor_pagar = num_galao * 25


# Saída de dados:

print(f"- área de cobertura: {m2}")
print(f"- número de galões: {num_galao}")
print(f"- valor a ser pago: R$ {valor_pagar:.2f}")
