print('')
o = int(input('Digite um numero: '))
print(o)

u = o // 1 % 10
d = o // 10 % 10
c = o // 100 % 10 
m = o // 1000 % 10

print('Analisando o numero {}'.format(o))
print(f'Unidade:{u}')
print(f'Dezena:{d}')
print(f'centena:{c}')
print(f'Milhar:{m}')

print('')