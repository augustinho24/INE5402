n = int(input())

vencedor_p_rodada = []

for _ in range(n):
    
    pos_vencedor = 0
    valor_d_vencedor = 0
    
    qt, s = [int(x) for x in input().split()]
    jogadores = [int(k) for k in input().split()]
    
    if len(jogadores) == qt:
        
        for i in range(0,len(jogadores)):
            if abs(jogadores[i] - s) < abs(valor_d_vencedor - s):
                pos_vencedor = i+1
                valor_d_vencedor = jogadores[i]
                
        vencedor_p_rodada.append(pos_vencedor)
        
print(*vencedor_p_rodada, sep= '\n')



