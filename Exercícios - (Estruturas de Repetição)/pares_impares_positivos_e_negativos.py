pares = 0
impares = 0
positivos = 0
negativos = 0 

for a in range (5):
    n = int(input())
    if n % 2 == 0:
        pares += 1
    if n % 2 != 0:
        impares += 1
    if n > 0:
        positivos += 1
    if n < 0:
        negativos += 1

        
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")



    