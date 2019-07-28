n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Com as notas {n1:.1f} e {n2:.2f}, a média do aluno é {m:.1f}')

if m <= 5:
    print(f'O aluno está REPROVADO')
elif m >= 5 and m <= 6.9:
    print(f'O aluno está em RECUPERAÇÃO')
elif m > 7:
    print(f'O aluno está APROVADO')