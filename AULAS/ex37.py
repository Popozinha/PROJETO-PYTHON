num = int(input('digite um numero inteiro: '))
print (''' escolha uma das conversões abaixo
       [1] converter em bínarío
       [2] converter em octal
       [3] converter em hexadecimal''')

opção = int(input('Sua escolha: '))

if opção == 1:
    print('{} convertido em binario fica {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida. Tente novamente')

