
n = int(input())
for r in range(n):
    soma = 0
    x = int(input())
    for val in range(1,x):
        if x % val == 0:
            soma += val
    if soma==x: 
        print(f"{x} eh perfeito")
            
    else:
        print(f"{x} nao eh perfeito")
            
            
            
            


