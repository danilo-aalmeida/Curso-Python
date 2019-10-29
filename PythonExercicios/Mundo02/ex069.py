print('-' * 30)
cadastre = 'Cadastro de Pessoas'
print(f'{cadastre: ^30}')
print('-' * 30)

tot18 = 0
totH = 0
totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'H':
        totH += 1
    if sexo == 'M' and idade < 20:
        totM20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {tot18}. \n'
      f'Ao todo temos {totH} homens cadastrados. \n'
      f'E temos {totM20} mulheres com menos de 20 anos.')
