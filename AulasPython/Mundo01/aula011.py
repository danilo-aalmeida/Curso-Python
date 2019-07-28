
# \033[0;33;44m
# \033[estilo; texto; background m

# Estilo:
# 0 >> Nenhum; 
# 1 >> Negrito; 
# 4 >> Sublinhado; 
# 7 >> Negativo

##Texto: 'Cor do texto'
#30 >> Branco
#31 >> Vermelho
#32 >> Verde
#33 >> Amarelo
#34 >> Azul
#35 >> Magenta
#36 >> Cyan
#37 >> Cinza

## Background: 'Cor do fundo'
#40 >> Branco
#41 >> Vermelho
#42 >> Verde
#43 >> Amarelo
#44 >> Azul
#45 >> Magenta
#46 >> Cyan
#47 >> Cinza

print('\033[0;30;41m Teste!')
print('\033[4;33;44m Teste!')
print('\033[1;35;43m Teste!')
print('\033[30;42m Teste!')
print('\033[m Teste!')
print('\033[7;36;44m Teste!')

nome = 'Danilo'
cores = {'limpa': '\033[0;0;0m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
                    'pretoebranco': '\033[7;30m'}

print(f'Olá! Muito prazer em te conhecer, {cores["amarelo"]} {nome} {cores["limpa"]}!!!')
