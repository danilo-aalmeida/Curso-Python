for c in range(1,6):
    maior = 0
    menor = 0
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior:.2f}Kg')
print(f'O menor peso lido foi de {menor:.2f}Kg')