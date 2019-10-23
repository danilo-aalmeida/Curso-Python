from math import factorial
numero = int(input('Digite um número para calcular seu Fatorial: '))
# fatorial = factorial(numero)
# print(f'O fatorial de {numero} é {fatorial}')
fatorial = 1
print(f'Calculando {numero}! =')
c = numero
while c > 0:
    print(f'{c}', enc='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1