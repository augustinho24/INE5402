valor_veiculo = float(input())
desconto_bruto = valor_veiculo*0.1
sexo = input().upper()
idade = int(input())
premio_seguro = 0

if sexo == 'M':
    
    if idade <= 24:
        premio_seguro = desconto_bruto
        print(f"{premio_seguro:.2f}")
        
    elif idade >= 25 and idade <= 33:
        premio_seguro = desconto_bruto - (desconto_bruto* 0.1)
        print(f"{premio_seguro:.2f}")
    
    elif idade > 33:
        premio_seguro = desconto_bruto - (desconto_bruto * 0.2)
        print(f"{premio_seguro:.2f}")

elif sexo == 'F':
    
    if idade <= 24:
        premio_seguro = desconto_bruto - (desconto_bruto * 0.05)
        print(f"{premio_seguro:.2f}")
        
    elif idade >= 25 and idade <= 33:
        premio_seguro = desconto_bruto - (desconto_bruto * 0.2)
        print(f"{premio_seguro:.2f}")
    
    elif idade > 33:
        premio_seguro = desconto_bruto - (desconto_bruto * 0.35)
        print(f"{premio_seguro:.2f}")
    
else:
    print("None.")
        