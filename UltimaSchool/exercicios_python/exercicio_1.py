a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))
c = int(input('Digite o terceiro número inteiro: '))

lista = [a, b, c]

for numero in lista:
    if numero == max(lista):
        print(f'Este é o maior número: {numero}')
    elif numero == min(lista):
        print(f'Este é o menor número: {numero}')
    else:
        print(f'Este é o número intermediário: {numero}')
