num_apostados = [int(x) for x in input().split()]
num_sorteados = [int(x) for x in input().split()]
acertos = 0


'''i = 0
j = len(num_sorteados)-1
while i < len(num_apostados) and j >= 0:
    if num_apostados[i] == num_sorteados[j]:
        acertos += 1
        i += 1
        j -= 1
    elif num_apostados[i] < num_sorteados[j]:
        i += 1
    else:
        j -= 1'''

#  Melhor:|
#         |
#         V
for i in range(len(num_sorteados)):
    if num_sorteados[i] in num_apostados:
        acertos += 1

if acertos < 3:
    print("azar")
elif acertos == 3:
    print("terno")
elif acertos == 4:
    print("quadra")
elif acertos == 5:
    print("quina")
else:
    print("sena")

