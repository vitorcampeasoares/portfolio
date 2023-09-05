class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def coleta_dados(self):
        cliente.nome = input('Insira o nome do cliente: ')
        cliente.cpf = input('Insira o cpf do cliente: ')
        cliente.idade = input('Insira a idade do cliente: ')

    def imprime_dados(self):
        print('Nome: {cliente.nome} CPF {cliente.cpf} Idade {cliente.idade}')


contador = 0
cliente = Cliente

while contador <= 5:
    cliente.coleta_dados(cliente)
    cliente.imprime_dados(cliente)
    contador += 1
