escala_origem = input().upper()
valor_temperatura_origem = float(input())  
escala_destino = input().upper()
converte_celsius = 0

if escala_origem == 'C':
    converte_celsius = valor_temperatura_origem
    
    if escala_destino == 'C':
        temperatura = converte_celsius
        print(f"{temperatura}")
    
    elif escala_destino == 'F':
        temperatura = (converte_celsius * 1.8) + 32
        print(f"{temperatura}")
        
    elif escala_destino == 'K':
        temperatura = converte_celsius + 273.15
        print(f"{temperatura}")
    
    elif escala_destino == 'R':
        temperatura = (converte_celsius + 273.15) * 9/5
        print(f"{temperatura}")
        
elif escala_origem == 'F':
    converte_celsius = (valor_temperatura_origem - 32) / 1.8
    
    if escala_destino == 'C':
        temperatura = converte_celsius
        print(f"{temperatura}")
    
    elif escala_destino == 'F':
        temperatura = (converte_celsius * 1.8) + 32
        print(f"{temperatura}")
    
    elif escala_destino == 'K':
        temperatura = converte_celsius + 273.15
        print(f"{temperatura}")
    
    elif escala_destino == 'R':
        temperatura = (converte_celsius + 273.15) * 9/5
        print(f"{temperatura}")

elif escala_origem == 'K':
    converte_celsius = valor_temperatura_origem - 273.15
    
    if escala_destino == 'C': 
        temperatura = converte_celsius
        print(f"{temperatura}")
        
    elif escala_destino == 'F':
        temperatura = (converte_celsius * 1.8) + 32
        print(f"{temperatura}")
    
    elif escala_destino == 'K':
        temperatura = converte_celsius + 273.15
        print(f"{temperatura}")
    
    elif escala_destino == 'R':
        temperatura = (converte_celsius + 273.15) * 9/5
        print(f"{temperatura}")

elif escala_origem == 'R':
    converte_celsius = (valor_temperatura_origem * 5/9) - 273.15
    
    if escala_destino == 'C':
        temperatura = converte_celsius
        print(f"{temperatura}")
    
    elif escala_destino == 'F':
        temperatura = (converte_celsius * 1.8) + 32
        print(f"{temperatura}")
    
    elif escala_destino == 'K':
        temperatura = converte_celsius + 273.15
        print(f"{temperatura}")
    
    elif escala_destino == 'R':
        temperatura = (converte_celsius + 273.15) * 9/5
        print(f"{temperatura}")