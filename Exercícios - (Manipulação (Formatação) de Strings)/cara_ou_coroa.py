while True:
    num_rodadas = int(input())
    if num_rodadas == 0:
        break
    else: 
        maria = 0
        joao = 0
        rodada = str(input())
        rodada = rodada.replace(" ", "")

        if num_rodadas != len(rodada):
            print("none")
        else:
            maria += rodada.count("0")
            joao += rodada.count("1")
        print(f"Mary won {maria} times and John won {joao} times")