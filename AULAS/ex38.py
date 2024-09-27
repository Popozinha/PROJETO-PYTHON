from time import sleep
print('')
n1 = float(input('\033[32m Diga um valor: \033[m'))
n2 = float(input('\033[33m Diga mais um valor: \033[m'))
print('')
print('\033[1;46m PROCESSANDO A RESPOSTA \033[m')

sleep(2)

print('')
if n1 > n2:
  print('\033[1;35m O maior numero é o primeiro\033[m')
elif n2 >n1:
  print('\033[1;36m O maior numero é o segundo\033[m')
else:
  print('\033[1;32m Os numeros são iguais\033[m')

print('')
sleep(2)

mt = n1 * n2
sm = n1 + n2
sb = n1 - n2
dv = n1 / n2

print('''\033[33m Podemos ver algumas fomas matematicas? 
    [1] MULTIPLICAÇÃO
    [2] SOMA
    [3] SUBRITRAÇÃO
    [4] DIVISÃO \033[m''')
opção = input('\033[34m Diga-nos a sua opção: \033[m')

if opção == '1':
  print('\033[1;30;44m O resultado da MULTIPLICAÇÃO entre o primeiro valor e o segundo foi:\033[m',mt)
elif opção == '2':
  print('\033[1;30;45m O resultado da SOMA  entre o primeiro valor e o segundo foi:\033[m',sm)
elif opção == '3':
  print('\033[1;20;42m O resultado da SUBRITRAÇÃO entre o primeiro valor e o segundo foi:\033[m',sb)
elif opção == '4':
  print('\033[1;30;43m O resultado da DIVISÃO entre o primeiro valor e o segundo foi:\033[m',dv)
else:
    print('Opção invalida')
print('')
print('\033[1;32;43m Sua curiosidade vai te levar sempre bem mais alto, Parabéns!\033[m')
print('')

import ex31

print('')


import ex35
print('')