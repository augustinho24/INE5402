N = int(input())
input()

for k in range(N):
    
    dicio_arvores = {}
    total_arvores = 0

    while True:
        try:
            especie_arvore = input().strip()
            
            if especie_arvore == '':
                break
            
            if especie_arvore not in dicio_arvores:
                dicio_arvores[especie_arvore] = 1
            else:
                dicio_arvores[especie_arvore] += 1
            total_arvores += 1

        except EOFError:
            break


    for nome in sorted(dicio_arvores.keys()):
        print(f'{nome} {100/total_arvores*dicio_arvores[nome]:.4f}')

    if k != N-1:
        print()







    




