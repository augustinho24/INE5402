n1 = float(input())
n2 = float(input())
n3 = float(input())

media = round((n1+n2+n3)/3,1)

if (media >= 9.0) and (media <= 10.0):
    print("Ótimo")

elif (media >= 7.5) and (media < 9.0):
    print("Bom")
    
elif (media >= 6.0) and (media < 7.5):
    print("Satisfatório")

elif (media == 0) or (media < 6.0):
    print("Insuficiente")