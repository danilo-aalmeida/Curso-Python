sexo = str(input(print('Informe o seu sexo [M/F]: '))).strip().upper()[0]
while(sexo not in 'MmFf'):
    sexo = str(input('Opção inválida, por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')




