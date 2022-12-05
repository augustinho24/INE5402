n_calouros = int(input())
lista_calouros = []
calouros_doadores = 0

for i in range(n_calouros):
    lista_calouros.append(input())

n_doadores = int(input())
lista_doadores = []

for i in range(n_doadores):
    lista_doadores.append(input())

for calouro in lista_calouros:
    if calouro in lista_doadores:
        calouros_doadores += 1

proporcao = calouros_doadores / n_calouros

print(f"{proporcao:.5f}")




