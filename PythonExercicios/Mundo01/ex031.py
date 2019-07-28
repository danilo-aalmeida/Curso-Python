distancia = float(input('Insira a distância (Km) da sua viagem: '))
print(f'Você esta prestes a começar uma viagem de {distancia}Km.')

if distancia > 200.0:
    preco = (distancia * 0.45)
else:
    preco = (distancia * 0.50)

print(f'E o preço da sua passagem será de R${preco:.2f}')