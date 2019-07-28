import random
aluno1 = input('Informe o nome do 1º aluno: ')
aluno2 = input('Informe o nome do 2º aluno: ')
aluno3 = input('Informe o nome do 3º aluno: ')
aluno4 = input('Informe o nome do 4º aluno: ')
alunos =[aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(alunos)

print(f'O aluno sorteado foi {sorteado}.')
