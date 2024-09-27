resp= 's'
s = c= m = maior = menor= 0
while resp in 'Ss':
    n= int(input('Diga um numero: '))
    s += n
    c+=1
    if c == 1:
        maior= menor = n
    else:
        if n>maior:
            maior=n
        if n <menor:
            menor= n
    resp= str(input('Quer continuar [N/S]: ')).upper().strip()[0]
m = s / c
print('vc digitou {} numeros a media foi {}'.format(c,m))
print('O maior numero é {} e o menor é {}'.format(maior,menor))
