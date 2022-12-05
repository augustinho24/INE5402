status = False
pontos = 0
c1 = input().upper()
c2 = input().upper()
c3 = input().upper()
c4 = input().upper()

if c1 == 'A':
    pontos += 4
elif c1 == 'B':
    pontos += 3
elif c1 == 'C':
    pontos += 2
elif c1 == 'E':
    pontos += 0

if c2 == 'A':
    pontos += 4
elif c2 == 'B':
    pontos += 3
elif c2 == 'C':
    pontos += 2
elif c2 == 'E':
    pontos += 0

if c3 == 'A':
    pontos += 4
elif c3 == 'B':
    pontos += 3
elif c3 == 'C':
    pontos += 2
elif c3 == 'E':
    pontos += 0

if c4 == 'A':
    pontos += 4
elif c4 == 'B':
    pontos += 3
elif c4 == 'C':
    pontos += 2
elif c4 == 'E':
    pontos += 0

if c1 == 'E' or c2 == 'E' or c3 == 'E' or c4 == 'E':
    status = False
    print(status)

elif pontos/4 >= 3:
    status = True
    print(status)

elif pontos/4 < 3:
    status = False
    print(status)
    
# print(pontos/4)
