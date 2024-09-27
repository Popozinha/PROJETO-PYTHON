from math import factorial
n = int(input('Diga um numero para calcular sua fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))

n = int(input('Diga um numero para calcular sua fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c>0:
    print('{}'.format(c),end='')
    print(' x ' if c>1 else ' = ',end='')
    f*=c
    c-=1
print('{}'.format(f))


n = int(input('Diga um numero para calcular sua fatorial: '))
print('Calculando {}! = '.format(n), end='')

for fatorial in range(1, 10, -1):
    print('{}'.format(n),end='')
    print(' x ' if fatorial>1 else ' = ',end='')
    f*=c
    c-=1
print('{}'.format(f))