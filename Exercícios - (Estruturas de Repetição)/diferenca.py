import math
confirma = False

def fat(x):
    if x == 0:
        return 1
    else:
        return x * fat (x-1)

n = 0

for a in range (10**3):
    n += 1
    if fat(n) > n**10:
        confirma = True
        print(n)
        break
 
    
    


    