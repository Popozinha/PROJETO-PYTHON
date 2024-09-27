print('')
from random import randint
from time import sleep
print('*=*' * 20)
print('TENTE ADIVINHAR EM QUAL NUMERO ESTOU PENSANDO...')
print('*=*' * 20)
no = int(input('Escreva um numero de 0 a 5: '))
ran = randint(0,5)
print('')
print('PROCESSANDO....')
sleep(3)
print('')
n = ('Eu estava pensando em {} '.format(ran))
print('')

print (n)
if no == ran:
    print('Você acertou')
else:
    print('Você não acertou')

print('')

