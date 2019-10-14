from random import randint
print('Sou seu computador...')
computador = randint(0,10)
print('Acabei de pensar em um número entre 0 e 10.\n'
      'Será que você consegue adivinhar qual foi?')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
if tentativas == 1:
    print('Ual, você acertou de primeira!! \n'
          f'O número pensado era {computador}.')
else:
    print(f'Você acertou com {tentativas} tentativas! \n'
          f'O número pensado era {computador}')

# jogador = int(input('Qual é o seu palpite?'))
# tentativa = 1
# while jogador != computador:
#     tentativa += 1
#     if jogador < computador:
#         jogador = int(input('Mais... Tente novamente:'))
#     else:
#         jogador = int(input('Menos... Tente novamente:'))
# 
# if tentativa > 1:
#     print(f'Parabéns, você acertou com {tentativa} tentativas! \n'
#           f'O número pensado era {computador}.')
# else:
#     print('Ual, você acertou de primeira!! \n'
#           f'O número pensado era {computador}.')