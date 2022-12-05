qtd_valores = int(input())
soma_nota = 0
contador = 0 
for a in range(qtd_valores):
    nota = float(input())
    soma_nota += nota
    contador += 1
    if contador == qtd_valores:
        media = soma_nota/qtd_valores
        print(f"{media:.3f}")
            
        
        