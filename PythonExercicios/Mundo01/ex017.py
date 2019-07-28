import math
catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))
# hipo = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
hipo = math.hypot(catOposto, catAdjacente)
print(f'A hipotenusa vai medir {hipo:.2f}')