valor_veiculo = float(input())
classe_desconto = input()
procedencia = input()
idade = int(input())

perc_premio = 0.1 if procedencia == 'nacional' else 0.15
premio_bruto = valor_veiculo * perc_premio

if classe_desconto == 'A':
    perc_desconto_classe = 0.3
elif classe_desconto == 'B':
    perc_desconto_classe = 0.2
elif classe_desconto == 'C':
    perc_desconto_classe = 0.1
elif classe_desconto == 'D':
    perc_desconto_classe = 0.05
else:
    perc_desconto_classe = 0
desconto_classe = premio_bruto * perc_desconto_classe

perc_desconto_idade = 0.1 if idade > 24 else 0
desconto_idade = premio_bruto * perc_desconto_idade

premio_liquido = round(premio_bruto - desconto_classe - desconto_idade)

print(f"{premio_liquido:.2f}")