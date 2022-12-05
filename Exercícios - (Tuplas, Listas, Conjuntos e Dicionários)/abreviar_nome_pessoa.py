
nomes = input().split()

for a in range(1, len(nomes) - 1):
    if len(nomes[a]) > 3:

        nomes[a] = nomes[a][0] + '.'
    
print(*nomes)



        
        
    