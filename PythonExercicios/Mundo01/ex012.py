preco = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Insira o (%) de desconto. '))
nPreco = preco - (preco * (desconto / 100))
print(f'O produto que custava R${preco:.2f}, na promoção de {desconto:.2f}% de desconto vai custar R${nPreco:.2f}.')