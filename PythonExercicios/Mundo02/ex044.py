print(f'{"="*20} LOJA PYTHON {"="*20}')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque.')
print('[ 2 ] à vista cartão.')
print('[ 3 ] 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    precoFinal = preco - (preco * 0.1)

elif opcao == 2:
    precoFinal = preco - (preco * 0.05)

elif opcao == 3:
    precoFinal = preco
    parcela = precoFinal / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')

elif opcao == 4:
    precoFinal = preco + (preco * 0.2)
    parcelas = int(input('Quantas parcelas? '))
    parcela = precoFinal / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parcela:.2f}')

else:
    print('Escolha uma opção válida!')

print(f'Sua compra de R${preco}, vai custar R${precoFinal} no final.')