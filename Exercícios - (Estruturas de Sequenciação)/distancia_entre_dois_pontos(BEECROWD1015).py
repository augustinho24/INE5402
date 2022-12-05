#Calcular a distância entre dois pontos

import math

x1, y1 = [float(k) for k in input().split()]
x2, y2 = [float(k) for k in input().split()]

distancia = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
print(f"{distancia:.4f}")

