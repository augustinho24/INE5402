n = int(input())
quebrados = 0

for a in range (n):
    l , c = [int(x) for x in input().split()]
    if l > c:
        quebrados += c
    elif l < c:
        pass
print(quebrados)


