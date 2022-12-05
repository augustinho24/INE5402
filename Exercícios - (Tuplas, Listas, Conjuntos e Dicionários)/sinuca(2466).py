N = int(input())

bolas = [int(x) for x in input().split()]

for i in range(len(bolas)-1):
    
    novas_bolas = []
    
    for j in range(len(bolas)-1):
        if bolas[j] == bolas[j+1]:
            novas_bolas.append(1)
        else:
            novas_bolas.append(-1)
    
    bolas.clear()
    bolas = novas_bolas.copy()

if 1 in bolas:
    print("preta")
else:
    print("branca")
