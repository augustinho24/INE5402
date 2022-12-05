#jogo xadrez movimento da rainha

pode_mover = False

x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]

if x1 == x2 or y1 == y2:
    pode_mover = True
elif abs(x1 - x2) == abs(y1 - y2):
    pode_mover = True
elif abs(x1 + x2) == abs(y1 + y2):
    pode_mover = True

print(pode_mover)



