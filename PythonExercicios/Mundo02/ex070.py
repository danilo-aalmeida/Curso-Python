print('=' * 40)
frase = 'Loja Super Baratão'
print(f'{frase:^40}')
print('=' * 40)

total_compra = totMil = menor_preco = contador = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total_compra += preco
    if preco > 1000:
        totMil += 1
    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('Fim da Compra'))
print(f'O total da compra foi R$ {total_compra:.2f}.')
print(f'Temos {totMil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi a(o) {produto} que custou R${menor_preco:.2f}.')
