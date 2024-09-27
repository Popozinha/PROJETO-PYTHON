from math import hypot

co = float(input('\033[34m Comprimento do cateto oposto: \033[m'))
ca = float(input('\033[32m Comprimento do cateto adjacente: \033[m'))
hi = hypot(co,ca)
print (f'\033[4;30;42mA hypot vai medir: {hi:.2f}\033[m')