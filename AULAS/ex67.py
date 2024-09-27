while True:
    n = int(input('diga um numero para a tabuada funcionar: '))
    if n <0:
        break
    for c in range (0, 11):
        print(f'{n} x {c} = {n*c}')
print('NÃO EXISTE TABUADA NEGATIVA, VOLTA PRA ESCOLA!')
print('APOOO')
