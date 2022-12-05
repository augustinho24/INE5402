#Ver se é triângulo ou não.

a = float(input())
b = float(input())
c = float(input())

sim_ou_nao = a + b > c and b + c > a and a + c > b
print(sim_ou_nao)



