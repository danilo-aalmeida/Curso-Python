import math
ang = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang)) 
tang = math.tan(math.radians(ang))

print(f'O ângulo de {ang} tem o SENO de {sen:.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tang:.2f}')