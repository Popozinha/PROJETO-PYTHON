from random import randint
'''contador = 0
print ('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10')
print('sera que vc consegue advinhar qual foi?')

computador= randint(0,10)
palpite =int(input('Qual seu palpite: '))
if palpite< computador:
    print('Mais.... tente novamente')
else:
    print('Menos..... tente novamente')  

while palpite != computador:
    palpite =int(input('Qual seu palpite: '))
    contador += 1
res = contador +1
print('Parabens {} tentativas'.format(res))
   '''  
computador = randint (0,10)
print ('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
print('sera que vc consegue advinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador =int(input('Qual seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... tente novamente')
        elif jogador > computador:
            print('Menos..... tente novamente') 
print('Parabens {} tentativas'.format(palpite))