frase = input().lower().split()

letras = {}

for palavra in frase:
    for letra in palavra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

maior = 0
for letra in letras:
    if letras[letra] > maior:
        maior = letras[letra]
        letra_mais_frequente = letra

print(letra_mais_frequente)

