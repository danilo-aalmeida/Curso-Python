multiplicador = resultado = 0
while True:
    valor = int(input('Você quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('=' * 20)
    for multiplicador in range(1, 11):
        resultado = valor * multiplicador
        print(f'{valor} x {multiplicador} = {resultado}')
    print('=' * 20)
