import math

primeiro_menor = math.inf
segundo_menor =  math.inf

x = int(input())

for c in range(x):
    
    x = int(input())
    

    if x <= primeiro_menor and x <= segundo_menor:
        segundo_menor = primeiro_menor
        primeiro_menor = x
        
    elif x > primeiro_menor and x < segundo_menor:
        segundo_menor = x
    
print(segundo_menor)
     
