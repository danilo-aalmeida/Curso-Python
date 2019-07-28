cores={'limpa':'\033[m',
'vermelho':'\033[1;31m',
'verde':'\033[1;32m'}

print('Insira TRÊS valores...')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

# Verificando o menor númmero
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor número é {cores["vermelho"]}{menor}{cores["limpa"]}.')
print(f'O maior número é {cores["verde"]}{maior}{cores["limpa"]}.')