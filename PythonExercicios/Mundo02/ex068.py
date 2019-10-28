from random import randint
vitorias = 0
print('=-' * 30)
frase = 'Vamos Jogar Par ou Impar!!!'
print(f'{frase:^60}')
print('=-' * 30)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
        print(f'Você escolheu {jogador} e o computador {computador}. \n'
              f'Total de {total}', end='')
        print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            vitorias += 1
        else:
            print('Você perdeu!!!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            vitorias += 1
        else:
            print('Você perdeu!!!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {vitorias} vezes.')
