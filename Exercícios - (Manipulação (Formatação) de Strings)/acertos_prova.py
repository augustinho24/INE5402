def correcao(x,y):
    acertos = 0
    gabarito = [str(quest) for quest in x if quest.isalpha()]
    mariazinha = [str(resp) for resp in y if resp.isalpha()]
    
    if len(gabarito) != len(mariazinha):
        print("NONE")

    else:
        for i in range (0, len(gabarito)):
            resposta = mariazinha[i]
            gabba = gabarito[i]
            if resposta == gabba:
                acertos += 1
            else:
                pass
        return acertos
  
julgamento = str(input())
reu = str(input())

print(correcao(julgamento,reu))


            
            
            