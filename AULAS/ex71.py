print('■'*20)
print('{:^20}'.format('BANCO POZINHO'))
print('■'*20)
valor= int(input('quanto vc quer sacar: R$  '))
total = valor
c = 50
tot = 0
while True:
    if valor >= c:
        valor-=c
        tot += 1
    else:
        if tot > 0:
            print(f'total de {tot} cédulas de R$ {c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tot = 0
        if tot == 0:
            break
print('■'*20)
print('volte sempre ao BANCO POZINHO!')

