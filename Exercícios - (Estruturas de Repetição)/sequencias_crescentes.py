while True:
    n = int(input())
    if n == 0:
        break

    seq = " "
    for e in range (1, n+1):
        seq += str(e) + " "
    print(seq)
