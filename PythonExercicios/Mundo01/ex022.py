nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
primeiro = nome.split()
print(f'Seu primeiro nome é {primeiro[0]} tem ao todo {len(primeiro[0])} letras')