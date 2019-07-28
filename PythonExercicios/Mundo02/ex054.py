from datetime import datetime
atual = datetime.now().year
menor = 0
maior = 0
for c in range(1,8):
    ano = int(input(f'Qual é o ano de nascimento da {c}ª pessoa? '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor +=1
print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')