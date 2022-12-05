def romano_decimal(num_romano):
    decimal = 0
    for i in range(len(num_romano)):
        if i > 0 and valores_romanos[num_romano[i]] > valores_romanos[num_romano[i - 1]]:
            decimal += valores_romanos[num_romano[i]] - 2 * valores_romanos[num_romano[i - 1]]
        else:
            decimal += valores_romanos[num_romano[i]]
    return decimal


valores_romanos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
num_romano = input().upper()

decimal = 0


print(romano_decimal(num_romano))

