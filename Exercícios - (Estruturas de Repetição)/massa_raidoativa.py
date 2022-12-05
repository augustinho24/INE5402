
tempo = 0
vezes = 0
massa = float(input())

for a in range(0, 1000000):
    massa -= massa * 0.5
    vezes += 1
    if massa <= 0.2:
        print(vezes * 0)
        break

    elif massa < 0.5:
        print(vezes * 50)
        break

