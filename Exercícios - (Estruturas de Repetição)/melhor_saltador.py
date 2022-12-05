melhor_nome = ' '
melhor_salto = 0


qtd_atletas = int(input())

for cu in range (1, qtd_atletas+1):
    s1,s2,s3, nome = input().split()
    s1 = float(s1)
    s2 = float(s2)
    s3 = float(s3)
    nome = str(nome)
    
    if s1 > melhor_salto:
        melhor_nome = nome
        melhor_salto = s1
    if s2 > melhor_salto:
        melhor_nome = nome
        melhor_salto = s2
    if s3 > melhor_salto:
        melhor_nome = nome
        melhor_salto = s3
                                        
    else:
        pass 

print(melhor_nome)
        
    
    