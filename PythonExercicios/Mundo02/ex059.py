from time import sleep
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
opcao = 0
while opcao != 5:
    print('Insira uma operação a ser realizada com os números: \n '
          '[1] Somar \n'
          '[2] Multiplicar \n'
          '[3] Maior \n'
          '[4] Novos Números \n '
          '[5] Sair do programa')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = (n1 + n2)
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        produto = (n1 * n2)
        print(f'O resultado de {n1} x {n2} é {produto}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe os números novamente')
        int(input('Insira o primeiro número: '))
        int(input('Insira o segundo número: '))
    elif opcao == 5:
        print('Programa finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa!')