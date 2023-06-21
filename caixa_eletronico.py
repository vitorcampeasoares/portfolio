def depositar():
    while True:
        valor = float(input('''Digite o valor que deseja depositar
ou 0 para sair.\n'''))
        if valor < 0:
            print('Valor inválido. Digite novamente.')
        elif valor == 0:
            break
        else:
            extrato.append(f'Depósito: R$ {valor:.2f}')
            return valor


def sacar():
    while True:
        valor = float(input('''Digite o valor que deseja sacar
ou 0 para sair.\n'''))
        if valor < 0:
            print('Valor inválido. Digite novamente.')
        elif valor > 500:
            print('O valor máximo desta operação é de R$ 500.00.')
        elif valor > saldo:
            print(f'Saldo insuficiente. Saldo disponível: R$ {saldo}')
        elif valor == 0:
            break
        else:
            extrato.append(f'Saque: R$ {valor}')
            return valor


saldo = 0
extrato = []
quantidade_de_saques = 0

while True:
    menu = int(input('''
        ### Seja Bem-vindo ###

        Qual Operação Deseja Fazer?

        1 - Deposito

        2 - Saque

        3 - Extrato

        0 - Sair

    '''))

    if menu == 1:
        deposito = depositar()
        if deposito is not None:
            saldo += deposito
            print(f'Depósito de R$ {deposito:.2f} realizado com sucesso.')
    elif menu == 2:
        if quantidade_de_saques < 3:
            saque = sacar()
            if saque is not None:
                saldo -= saque
                quantidade_de_saques += 1
                print(f'Saque de R$ {saque:.2f} realizado com sucesso.')
        else:
            print('Limite de 3 saques diários atingido')
    elif menu == 3:
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
            print('### Extrato Bancário ###')
            for movimentacao in extrato:
                print(movimentacao)
        print(f'Seu Saldo Atual é de R$ {saldo:.2f}')

    elif menu == 0:
        break

    else:
        print('Opção não encontrada, favor escolher entre uma das opções.')
