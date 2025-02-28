conta_normal = False
conta_universitaria = False
conta_especial = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insufiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insufiente!")
elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato como seu gerente.")