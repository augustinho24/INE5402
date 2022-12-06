def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
 

 
x = int(input())
y = int(input())
        
gcd, x, y = extended_gcd(x, y)
print(f'the GCD is {gcd}')
print(f'x = {x}, y = {y}')