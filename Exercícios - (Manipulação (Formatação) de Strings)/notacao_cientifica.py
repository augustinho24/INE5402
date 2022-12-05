import math

n = float(input())

while n > 0: # Casos quando n > 0 
    exp = round(math.log(n, 10))
    if exp > 0:
        exp = exp - 1
    else:
        pass
    
    if n >= 10:
        while n >= 10:
            n /= 10   
        print(f"+{n:.4f}E+{exp:02}")
        break
    
    elif n < 10:
        while n < 10:
            n *= 10
        if exp < 0:
            print(f"+{(n/10):.4f}E{exp:02}")
        else:
            print(f"+{(n/10):.4f}E+{exp:02}")
        break
    
while n < 0: # Casos quando n < 0
    n_negativo = n
    n = n * -1
    exp = round(math.log(n, 10))
    if exp < 0:
        exp = exp * -1
    else:
        pass
            
        
    if n >= 10:
        while n > 10:
            n /= 10   
        print(f"-{n:.4f}E+{exp:02}")
        break
    
    elif n < 10:
        while n < 10:
            n *= 10
        print(f"-{(n/10):.4f}E-{exp:02}")
        break
    
    
        
    
        

    
