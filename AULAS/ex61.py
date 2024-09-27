ponto = int(input('Diga seu primeiro termo: '))
razão = int(input('Diga sua razão: '))

termo = ponto
cont = 1
while cont <=10:
    print ('{} -> '.format(termo), end='')
    termo+= razão
    cont += 1
print('Acabou')