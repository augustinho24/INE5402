n = int(input())

for i in range(n):
    palavra_final = ''
    palavras = input().split()
    primeira_palavra = palavras[0]
    segunda_palavra = palavras[1]

    for i in range(len(primeira_palavra)):
    # adiciona a primeira letra da primeira palavra
        palavra_final += primeira_palavra[i]
    # adiciona a primeira letra da segunda palavra
        palavra_final += segunda_palavra[i]
        if i == len(primeira_palavra) - 1:
            break
        if i == len(segunda_palavra) - 1:
            break
    # se a primeira palavra for maior que a segunda, adiciona o resto da primeira palavra
    if len(primeira_palavra) > len(segunda_palavra):
        palavra_final += primeira_palavra[i+1:]
    # se a segunda palavra for maior que a primeira, adiciona o resto da segunda palavra
    elif len(segunda_palavra) > len(primeira_palavra):
        palavra_final += segunda_palavra[i+1:]
    print(palavra_final)
    

        
  