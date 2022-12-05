n1 = int(input())
n2 = int(input())

resto = n1 % n2
while resto > 0:
    n1 = n2
    n2 = resto
    resto = n1 % n2
print (n2)