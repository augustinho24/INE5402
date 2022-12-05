try:
    while True:
        teste = 'GRACE HOPPER'
        texto = input().upper().split('-')
        vovo = 'COBOL'
        
        for j in range(len(vovo)):
            
            if texto[j][0] not in vovo[j] and texto[j][-1] not in vovo[j]:
                teste = 'BUG'
        print(teste)
except EOFError:      
    pass