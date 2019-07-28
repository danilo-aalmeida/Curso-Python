#import math
from math import sqrt
import emoji
numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print(emoji.emojize(f'A raiz de {numero} é igual a {raiz:.2f} :v:',use_aliases=True))
