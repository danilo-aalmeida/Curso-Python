from random import randint
from time import sleep

print('~*' * 20)
print('{:^40}'.format(' PEDRA x PAPEL x TESOURA'))
print('~*' * 20)
itens = ('PEDRA','PAPEL','TESOURA')

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

computador = randint(0,2)
jogador = int(input('Qual é a sua jogada? '))

print('JO', end = '')
sleep(0.3)
print('.', end = '')
sleep(0.3)
print('.', end = '')
sleep(0.3)
print('.', end = '')
sleep(0.3)
print('KEN', end = '')
sleep(0.3)
print('.', end = '')
sleep(0.3)
print('.', end = '')
sleep(0.3)
print('.', end = '')
sleep(0.3)
print('PO!!!')
sleep(1)

print('-=' * 20)
print(f'   O computador escolheu {itens[computador]}')
print(f'    O jogador escolheu {itens[jogador]}')
print('-=' * 20)

if computador == 0: #Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')