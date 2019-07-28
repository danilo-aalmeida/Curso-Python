n = int(input('Insira um número para ver sua tabuada: '))
print('-' * 12)
i = 0
while True:
    r = n * i
    print(f'{n} x {i:2} = {r}')
    i = i + 1
    if(i>10):
        break
print('-' * 12)