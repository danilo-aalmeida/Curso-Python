peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura **2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc <= 18.5:
    print('Essa pessoa está ABAIXO do peso!')
elif imc > 18.5 and imc <= 25:
    print('Essa pessoa está com o peso IDEAL!')
elif imc > 25 and imc <= 30:
    print('Essa pessoa está com SOBREPESO!')
elif imc > 30 and imc <= 40:
    print('Essa pessoa está com OBESIDADE!')
else:
    print('Essa pessoa está com OBESIDADE MÓRBIDA!')