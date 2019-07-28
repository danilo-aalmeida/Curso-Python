velo = float(input('Qual é a velocidade atual do carro? '))
if velo > 80.0:
    multa = (velo - 80.0) * 7
    print('MULTADO! Voce excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')

    