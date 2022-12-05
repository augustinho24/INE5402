p1 = input()
p2 = input() 
valor_verdade = True

if p1 == p2:
    valor_verdade = False
    print(valor_verdade)

else:
    for a in p1:
        if sorted(p1) == sorted(p2):
            valor_verdade = True
            print(valor_verdade)
            break
        else:
            valor_verdade = False
            print(valor_verdade)
            break
