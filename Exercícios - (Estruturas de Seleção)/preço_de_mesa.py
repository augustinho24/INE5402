comprimento = float(input())
largura_mesa = float(input())
num_gavetas = int(input())
tipo_madeira = input().lower()

m2 = comprimento * largura_mesa

if (m2 > 2):
    preco = (m2*100) + (num_gavetas * 30) + 50
    
    if preco < 200:
        preco = 200
        if tipo_madeira == 'mogno':
            preco_mogno = preco + 150
            print(f"{preco_mogno:.1f}")
        elif tipo_madeira == 'carvalho':
            preco_carvalho = preco + 125
            print(f"{preco_carvalho:.1f}")
        else:
            print(f"{preco:.1f}") 
    
    if tipo_madeira == 'mogno':
        preco_mogno = preco + 150
        print(f"{preco_mogno:.1f}")
        
    elif tipo_madeira == 'carvalho':
        preco_carvalho = preco + 125
        print(f"{preco_carvalho:.1f}")
        
    else:
        print(f"{preco:.1f}")

elif (m2 < 2):
    
    preco = (m2*100) + (num_gavetas * 30) 
    
    if tipo_madeira == 'mogno':
        preco_mogno = preco + 150
        print(f"{preco_mogno:.1f}")
        
    elif tipo_madeira == 'carvalho':
        preco_carvalho = preco + 125
        print(f"{preco_carvalho:.1f}")
        
    if preco < 200:
        preco = 200
        
        if tipo_madeira == 'mogno':
            preco_mogno = preco + 150
            print(f"{preco_mogno:.1f}")
        
        elif tipo_madeira == 'carvalho':
            preco_carvalho = preco + 125
            print(f"{preco_carvalho:.1f}")
        else:
            print(f"{preco:.1f}") 
        
    




