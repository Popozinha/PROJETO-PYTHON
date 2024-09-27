
from time import sleep
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))

op5 = False
while not op5:
    sleep(1)
    print('''primeiro valor
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa''')
    chance = int(input('>>> Qual sua opção: '))
    print('\033[32m-==-\033[m'*10)
    if chance == 1:
        c = a+b
        print('O resultado é {}'.format(c))
    if chance == 2:
        d = a*b
        print('O resultado é {}'.format(d))
    if chance == 3:
        if a>b:
            maior=  a
        if b>a:
            maior = b
        print('Entre {} e {} o maior é {}'.format(a,b,maior))
    if chance ==4:
        a = int(input('primeiro valor: '))
        b = int(input('segundo valor: '))
    if chance == 5:
        op5 = True
        print('Programa finalizado')

