n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, \n o produto é {m} \n e a divisão é {d:.2f}.', end=' ')
print(f'A divisão inteira é {di} \n e a potência é {e}')
