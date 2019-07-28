num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    binario = bin(num)
    print(f'{num} convertido para BINÁRIO é igual a {binario[2:]}') #fatiamento de string
elif opcao == 2:
    octal = oct(num)
    print(f'{num} convertido para OCTAL é igual a {octal[2:]}')
elif opcao == 3:
    hexa = hex(num)
    print(f'{num} convertido para HEXADECIMAL é igual a {hexa[2:]}')
else:
    print('Escolha uma opção válida!')