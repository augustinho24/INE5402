
qtd_marias = 0

qtd_nomes = int(input())

for j in range (0, qtd_nomes):
    nome_atual = str(input()).lower()
    nome_atual = nome_atual.replace(" ", "")
    if nome_atual.count("marian") == 0:
        qtd_marias += nome_atual.count("maria")
    else:
        pass
print(qtd_marias)