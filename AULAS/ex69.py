t18=tm=tf= 0
 
while True:
    print('=-'*20)
    print('        -=CADASTRE UMA PESSOA-=')
    print('=-'*20)
    idade= int(input('Qual sua idade: '))
    s = ' '
    while s not in 'FM':
        s = str(input('diga seu sexo [F|M]: ')).strip().upper()[0]
    if idade >=18:
        t18+=1
    if s== 'M':
        tm+= 1
    if s == 'F' and idade <20:
        tf+=1
    t= ' '
    while t not in 'SN':
        t= input('quer continuar [S|N]: ').upper()
    if t == 'N':
        break

print('')
print(f'{t18} pessoas maiores de 18 anos')       
print(f'Ao todo temos {tm} homens cadastrados')
print(f'Ao todo temos {tf} mulheres com menos de 20 anos cadastradas')

print('apooo')

