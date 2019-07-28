s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < (s2 + s3) and s2 < (s1 + s3) and s3 < (s1 + s2):
    print(f'Os segmentos acima PODEM FORMAR um triângulo ', end ='')
    if s1 == s2 and s2 == s3:
       print('EQUILÁTERO!')
    if s1 != s2 and s2 != s3 and s1 != s3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo!')