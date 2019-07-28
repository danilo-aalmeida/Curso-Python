salario = float(input('Insira o salário atual do funcionário: R$'))
ajuste = float(input('Insira o (%) de aumento: '))
novoSalario = salario + (salario * (ajuste/100))
print(f'Um funcionário que ganhava R${salario:.2f}, com {ajuste:.2f}% de aumento, passa a receber R${novoSalario:.2f}')