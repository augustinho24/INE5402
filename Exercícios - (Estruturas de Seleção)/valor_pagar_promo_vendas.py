compra = float(input())

if compra < 500:
    desconto = compra - (compra * 0.2)
    print(f'{desconto:.2f}')

elif compra >= 500 and compra < 1000:
    desconto = compra - ((compra* 0.2) + (compra * 0.1))
    print(f'{desconto:.2f}')

elif compra >= 1000:
    desconto = compra - ((compra * 0.2) + (compra * 0.1) + ((compra - 1000) * 0.15))
    print(f'{desconto:.2f}')