n1 = float(input('Insira o primeiro número: '))
n2 = float(input('Insira o sehundo número: '))

if n1 > n2:
    print(f'O primeiro valor é maior')
elif n2 > n1:
    print(f'O segundo valor é maior')
else:
    print('Não existe valor maior, ambos são iguais:')
