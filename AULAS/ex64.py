'''n = c = soma = 0
n = int(input('Diga um numero[999 para parar]: '))
while n != 999:   
    soma+=n
    c+=1
    n = int(input('Diga um numero[999 para parar]: '))
print('vc digitou {} e a soma é {}'.format(c,soma))

'''###########################################################
u = contado = sub = 0
u = int(input('Diga um numero [0 para parar]: '))
while u != 0:
    sub= sub * u
    contado+=1
    u = int(input('Diga um numero [0 para parar]: '))
print("vc digitou {} e a subitração foi {}".format(contado,sub))
