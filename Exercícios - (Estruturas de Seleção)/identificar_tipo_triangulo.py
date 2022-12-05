a = int(input())
b = int(input())
c = int(input())

if (a == b == c):
    print("equilátero")

elif (a == b or b == c or a == c):
    print("isósceles")

elif ((a != b) and (b != c) and (a != c)):
    print("escaleno")

