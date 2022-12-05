frase = input()

frase_limpa = ''
for letra in frase.lower():
    if letra.isalpha():
        frase_limpa += letra

ver_palindromo = (frase_limpa == frase_limpa[::-1]) 

print(ver_palindromo)