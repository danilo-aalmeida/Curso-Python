cores = {'limpa': '\033[0;0;0m',
         'verde': '\033[1;37;42m',
         'vermelho': '\033[1;37;41m',
         'amarelo': '\033[1;33;44m',
         'magenta': '\033[1;35m'}

print(f'{cores["amarelo"]}-=-' * 20)
print(f'{cores["magenta"]} Analisador de Triângulos')
print(f'{cores["amarelo"]}-=-' * 20)
print('Insira o valor de TRÊS segmentos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print(
        f'Os segmentos acima {cores["verde"]}PODEM FORMAR{cores["limpa"]} um triângulo!')
else:
    print(
        f'Os segmentos acima {cores["vermelho"]}NÃO PODEM FORMAR{cores["limpa"]} um triângulo!')
