frase = '   Curso em Vídeo Python   '
print('- ', frase)
print('- ', frase[3])
print('- ', frase[3:13])
print('- ', frase[:13])
print('- ', frase[13:])
print('- ', frase[1:15:2])
print('- ', frase[1::2])
print('- ', frase[::2])
print('- ', frase.count('o'))
print('- ', frase.upper().count('O'))
print('- ', len(frase))
print('- ', len(frase.strip()))
print('- ', frase.replace('Python', 'Android'))
#frase = frase.replace('Python', 'Android')
print('- ','Curso' in frase)
print('- ',frase.find('Python'))
print('- ',frase.find('vídeo'))
print('- ',frase.lower().find('video'))
print('- ',frase.split())
dividido = frase.split()
print('- ', dividido[0])
print('- ', dividido[1])
print('- ', dividido[2])
print('- ', dividido[3])
print('- ', dividido[2][3])

print("""- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")