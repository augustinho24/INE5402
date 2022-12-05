preco = int(input())

if preco < 500:
    desconto = preco - (preco * 0.2)
elif preco >= 500:
    desconto = preco - ((preco * 0.2) + (preco * 0.1))
elif preco >= 1000:
    desconto = preco -  ((preco * 0.2) + (preco * 0.1) + ((preco - 1000) * 0.15))

print(f"{desconto:.2f}")