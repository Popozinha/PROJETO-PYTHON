print('')
from math import radians, sin, cos, tan
angulo = float(input('\033[32;46m Digite o ângulo que você deseja:  \033[m'))
seno = sin(radians(angulo))
print(f'\033[36m O ângulo de {angulo} tem o SENO de {seno:.2f}\033[m')
cosseno = cos(radians(angulo))
print(f'\033[32m O âgulo de {angulo} tem o COSSENO de {cosseno:.2f}\033[m')
tangente = tan(radians(angulo))
print(f'\033[31m O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}\033[m')
print('')