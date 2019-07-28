from datetime import datetime
nome = str(input('Qual é o seu nome? '))
hora = datetime.now()

if hora.hour >= 0 and hora.hour < 13:
    saudação = 'um bom dia'
elif hora.hour >= 13 and hora.hour < 18:
    saudação = 'uma boa tarde'
else:
    saudação = 'uma boa noite'

print(f'Tenha {saudação}, {nome}!!')