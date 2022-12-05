
nota = float(input())

parte_inteira = int(nota)
parte_nao_inteira = nota - parte_inteira

if parte_nao_inteira < 0.25:
    nota_final = parte_inteira
elif parte_nao_inteira < 0.75:
    nota_final = parte_inteira + 0.5
else:
    nota_final = parte_inteira + 1

print(nota_final)