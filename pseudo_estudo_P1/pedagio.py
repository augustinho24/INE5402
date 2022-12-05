L,D = [int(x) for x in input().split()]
K,P = [int(x) for x in input().split()]

qtd_pedágios_custo = (L//D) * P
custo_km = L*K
custo_total = custo_km + qtd_pedágios_custo

print(custo_total)