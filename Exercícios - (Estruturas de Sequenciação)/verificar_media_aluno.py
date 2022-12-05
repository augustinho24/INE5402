#Verificar se um estudante foi aprovado ou não.

def media_ponderada (nota1, nota2, nota3, peso1, peso2, peso3):
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    return media    

def entrada_dados():
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    peso1 = float(input())
    peso2 = float(input())
    peso3 = float(input())

    return nota1, nota2, nota3, peso1, peso2, peso3

nota1, nota2, nota3, peso1, peso2, peso3 = entrada_dados()
media = media_ponderada(nota1, nota2, nota3, peso1, peso2, peso3)
x = 6.0
print(media >= x)


        