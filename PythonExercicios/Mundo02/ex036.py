valorCasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salario do comprador? R$'))
tempo = int(input('Quantos anos de financiamento? '))

prestação = valorCasa / (tempo * 12)

if prestação > (salario * 0.3):
    situação = 'NEGADO'
else:
    situação = 'APROVADO'

print(f'Para pagar uma casa de R${valorCasa:.2f} em {tempo} anos, a prestação será de R${prestação:.2f}')
print(f'Empréstimo {situação}!')
