K = int(input())
NP = int(input())

provas = {}

for i in range(NP):
    cod_prova, gabarito = input().split()
    provas[cod_prova] = gabarito

candidatos = {}
NC = int(input())
for u in range(NC):
    nome, prova, respostas = input().split()

    candidatos[nome] = prova, respostas 

relacao_candidatos = {}

for nome, (prova, respostas) in candidatos.items():
    erros_seguidos = 0
    acertos = 0
    if prova in provas:
        relacao_candidatos[nome] = prova, respostas
        for i in range(len(provas[prova])):
            if provas[prova][i] == respostas[i]:
                acertos += 1
                erros_seguidos = 0
            else:
                erros_seguidos += 1
                if erros_seguidos == K:
                    relacao_candidatos[nome] = "reprovado"
                    break
        if erros_seguidos < K and acertos >= len(provas[prova]) * 0.75:
            relacao_candidatos[nome] = "aprovado"

for nome, indicacao in relacao_candidatos.items():
    print(nome, indicacao)

    

   

    
