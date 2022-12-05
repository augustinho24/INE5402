def binario_int(x):
    if x == 0:
        return '0'
    else:
        binario = ' '
        while x > 1:
            resto = x % 2
            x = int(x / 2)
            binario += str(resto)
        binario += '1'
    return binario[-1::-1]

n = int(input())
print(binario_int(n))

