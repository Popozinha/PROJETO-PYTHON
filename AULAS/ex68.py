from random import randint
v = 0
while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo= ' '
    while tipo not in 'PI':
        tipo= str(input('par ou impar: [P|I]: ')).strip().upper()[0]
    print(f'vc jogou {jogador} e o computador {computador} total foi {total}',end='')
    print(' DEU PAR'if total % 2 == 0 else  ' DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('vc venceu!')
            v+=1
        else:
            print('vc perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('vc venceu')
            v+=1
        else:
            print('vc perdeu')
            break
    print('Vamos continuar...')
print('GAME OVER! vc venceu {} vezes'.format(v))





