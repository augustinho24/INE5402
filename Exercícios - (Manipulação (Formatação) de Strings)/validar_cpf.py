
def digito_verificador(numero_com_dv):   
    soma = 0
    peso = len(numero_com_dv)
    for i in range(len(numero_com_dv)-1):
        soma += int(numero_com_dv[i]) * peso
        peso -= 1
    dv = 11 - soma % 11
    if dv >= 10:
        dv = 0

    return dv == int(numero_com_dv[-1])

cpf = input()
cpf_limpo = cpf.replace(".", "")
cpf_limpo = cpf_limpo.replace("-", "")

valido = len(cpf_limpo) == 11 and cpf_limpo.count(cpf_limpo[0]) != 11  and digito_verificador(cpf_limpo) and digito_verificador(cpf_limpo[:-1])
    
print(valido)

