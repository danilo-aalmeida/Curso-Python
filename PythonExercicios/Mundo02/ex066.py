soma = quantidade = 0
while True:
    valor = int(input('Digite um valor [999 para encerrar]'))
    if valor == 999:
        break
    soma += valor
    quantidade += 1
print(f'Você inseriu {quantidade} números e a soma deles é de {soma}')
