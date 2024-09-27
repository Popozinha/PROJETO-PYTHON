print('Gerador de PA')
print('=-' * 8)
primeiro = int(input('Primeiro terno: '))
razão = int(input('razão da PA: '))
terno = primeiro
cont = 1
while cont <= 10:
    print('{} => '.format(terno), end='')
    terno += razão
    cont += 1
print('Fim')
   