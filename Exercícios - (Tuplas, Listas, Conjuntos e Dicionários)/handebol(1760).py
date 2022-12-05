N, M = [int(x) for x in input().split()]

jogadores_que_marcaram_em_todo_jogo = 0

for i in range(N):
    lista_gols = [int(x) for x in input().split()]
    
    if 0 not in lista_gols:
        jogadores_que_marcaram_em_todo_jogo += 1

print(jogadores_que_marcaram_em_todo_jogo)