from banco import Banco

bc = Banco("Banco do Brejo", 999)

while True:

    entrada = input().split()
    if entrada == " ":
        break

    if entrada[0] == 'abre_conta':
        nome = entrada[2]
        cpf = entrada[1]
        bc.abre_conta(nome, cpf)
        print("Conta aberta com sucesso")

    elif entrada[0] == 'deposito':
        numero_conta = entrada[1]
        valor = entrada[2]
        bc.deposito(numero_conta, valor)
        print("Depósito realizado com sucesso")

    elif entrada[0] == 'transferencia':
        nct_origem = entrada[1]
        nct_destino = entrada[2]
        valor = entrada[3]
        bc.transferencia(nct_origem, nct_destino, valor)
        print("Transferência realizada com sucesso")

    elif entrada[0] == 'saque':
        numero_conta = entrada[1]
        valor = entrada[2]
        bc.saque(numero_conta, valor)
        print("Saque realizado com sucesso")



print(bc.exibir_contas())










'''bc = Banco("Banco do Brejo", 999)

ctj = bc.abre_conta("Joãozinho",987234)

ctm = bc.abre_conta("Mariazinha",135793)

bc.deposito (ctm, 150.00)
bc.deposito (ctj, 80.00)
bc.transferencia (ctm, ctj, 40.00)
bc.saque(ctm, 70.00)
bc.saque(ctj, 10.00)

print(bc.saldo(ctm))
print(bc.saldo(ctj))'''