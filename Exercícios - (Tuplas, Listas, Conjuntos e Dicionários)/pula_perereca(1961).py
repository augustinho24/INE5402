#pula perereca

caiu = " "

limite, qtdade = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]

for i in range (len(alturas) - 1):
    if abs(alturas[i]) + limite < abs(alturas[i+1]) : 
        caiu = True
        break

else:
    caiu = False

if caiu == True:
    print("GAME OVER")
else:
    print("YOU WIN")
