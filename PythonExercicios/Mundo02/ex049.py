num = int(input('Digite um número para ver sua tabuada: '))

for c in range(1,11):
    r = num * c
    print(f'{num} x {c} = {r}')
print('Fim')