menu = ''' ===== MENU ===== 
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    => '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))
    if opcao == 1:
        while True:
            deposito = float(input("Qual valor deseja depositar? R$ "))
            if deposito >= 500:
                print(f"O limite de depósito é de R$ {limite}. Tente de Novo!")
            else:
                saldo += deposito
                print(f"Depósito de R$ {saldo:.2f} realizado com sucesso!")
                extrato += f"Depósito: R$ {deposito:.2f} \n"
                break
    elif opcao == 2:
        while True:
            sacar = float(input("Qual valor deseja sacar? R$ "))
            if numero_saques >= 3:
                print("Saque indisponível!")
                break
            if sacar >= saldo:
                print("Saldo insuficiente. Tente de Novo!")
            else: 
                print(f"Saque de R$ {sacar:.2f} realizado com sucesso!")
                numero_saques += 1
                saldo -= sacar
                extrato += f"Saque: R$ {sacar:.2f} \n";
                break
    elif opcao == 3:
        if saldo > 0:
            print("=" * 30)
            print("{:^30} \n{}".format("EXTRATO", extrato))
            print("=" * 30)
            print(f'Seu saldo é de R$ {saldo:.2f}')
        if saldo == 0:
            print("=" * 30)
            print("{:^30}".format("EXTRATO"))
            print(f"Não foram realizadas movimentações.")
            print("=" * 30)
    elif opcao == 4:
        print("Obrigado por usar nosso sistema! Volte sempre!")
        break
    else:
        print("Opção inválida! Tente de Novo!")