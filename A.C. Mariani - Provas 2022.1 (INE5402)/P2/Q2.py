n = int(input())

casas = []
for i in range(n):
    casas.append(int(input()))
k = int(input())

"""for i in range(len(casas)-1):
    if casas[i+1] + casas[i] == k:
        print(casas[i],casas[i+1])
        break"""

casa1, casa2 = zip(*[(casas[i], casas[i+1]) for i in range(len(casas)-1) if casas[i+1] + casas[i] == k])
print(*casa1,*casa2)