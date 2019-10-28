print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} >> ', end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja mostrar? '))
print(f'Progressao finalizada com {total} termos mostrados.')
