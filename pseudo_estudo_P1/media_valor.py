n = int(input())
soma_notas = 0

for _ in range(n):
    val = float(input())
    soma_notas += val

media = soma_notas/n

print(f"{media:.3f}")
 