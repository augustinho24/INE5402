###

L,D=[int(cu) for cu in input().split()]
K,P=[int(cu) for cu in input().split()]

custo = (L*K) + ((L//D)*P)

print(custo)



