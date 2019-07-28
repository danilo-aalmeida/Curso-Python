'''nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Gustavo':
    print('Condição para Gustavo')
else:
    print('Condição para falso')
print(f'Olá, {nome};')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi de {m:.f}')
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude Mais')        