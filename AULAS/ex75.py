numero =    (int(input('diga um numero ')),
            int(input('diga um numero ')),
            int(input('diga um numero ')),
            int(input('diga um numero ')))
print(f'vc digitou os valores {numero}')
print(f'o valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3)+1}ª posição')
else:
    print('o numero 3 n apareceu')
print('os valores pares são ',end='')
for n in numero:
    if n % 2 == 0:
        print(n,end=' , ')

