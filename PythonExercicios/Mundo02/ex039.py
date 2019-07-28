from datetime import datetime
ano = int(input('Insira o ano de nascimento: '))
hoje = datetime.now().year
idade = hoje - ano
print(f'Quem nasceu em {ano} tem {idade} em {hoje}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {ano + 18}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano + 18}.')
