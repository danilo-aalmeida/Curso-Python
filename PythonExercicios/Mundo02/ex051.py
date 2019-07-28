print('=' * 10)
print('10 TEMPOS DE UMA P.A \n (PROGRESSÃO ARITIMÉRICA)')
print('=' * 10)
primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro, décimo + razao, razao):
    print('{} ',format(c), end='→ ')
print('ACABOU')