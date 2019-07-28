larg = float(input('Insira a largura da parede: '))
altu = float(input('Insira a altura da parede: '))
area = larg * altu
litr = area / 2 
print(f'Sua parede tem a dimensão de {larg:.2f}x{altu:.2f} e sua área é de: {area:.2f}m².')
print(f'Para pintar sua parede, você vai precisar de {litr:.1f}l de tinta.')