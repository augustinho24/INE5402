tot_positivos = 0
n_positivos = 0
n_inteiros = 0
while True:
    n = float(input())   
    if n == 0:
        break
    if (int(n) == n) == True:
        n_inteiros += 1
    if n > 0:
        tot_positivos += n
        n_positivos += 1
        
media_val_postivos = tot_positivos/n_positivos
print(f"número de valores inteiro: {n_inteiros}")
print(f"média dos valores postivos: {media_val_postivos:.2f}")
        
    
        
 