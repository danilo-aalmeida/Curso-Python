from datetime import datetime
ano = int(input('Ano de Nascimento: '))
atual = datetime.now().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JUNIOR'
elif idade > 19 and idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print(f'Classificação: {categoria}')
