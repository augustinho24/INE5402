#verificar tautograma

while True:
    tautograma = True
    frase = input()
    if frase == "*":
        break
    
    frase = frase.split()

    primeira_palavra = frase[0].lower()
    palavras = len(frase)  
    primeira_letra = primeira_palavra[0][0].lower()
    for i in range(palavras):
        if frase[i][0].lower() != primeira_letra:
            tautograma = False
            print("N")
            break
        else:
            continue
    if tautograma == True:
        print("Y")
    
    