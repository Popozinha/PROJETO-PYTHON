count = 0
n = int(input('digite um numero: '))
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end=' ')
        count = count + 1
        print(f'{c}', end=' ')
    else:
        print('\033[31m ', end=' ')
        print(f'{c}', end=' ')
print(f'\nO número {n} foi divisivel {count} vezes')
if count == 2:
    print('Ele é um numero primo')
else:
    print('Ele não é um numero primo')
