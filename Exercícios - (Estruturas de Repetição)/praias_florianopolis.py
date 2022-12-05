# Praias de Florianópolis

dist_praia_mais_distante = 0
nome_praia_mais_distante = " "
qtd_praias_entre_centro = 0
tot_distancia = 0
qtd_praias = int(input()) 

for r in range (qtd_praias):
    nome_praias, distancia_praia = input().split(';')
    distancia_praia = float(distancia_praia)
    tot_distancia += distancia_praia

    if distancia_praia > dist_praia_mais_distante:
        dist_praia_mais_distante = distancia_praia
        nome_praia_mais_distante = nome_praias

    if 15 <= distancia_praia <= 20:
        qtd_praias_entre_centro += 1

    media_distancia = tot_distancia / qtd_praias

print(f"{nome_praia_mais_distante};{qtd_praias_entre_centro};{round(media_distancia, 1)}")   