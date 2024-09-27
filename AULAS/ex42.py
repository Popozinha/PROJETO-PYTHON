r1 = float(input('Diga um número: '))
r2 = float(input('Diga o segundo número: '))
r3 = float(input('Diga o terceiro número: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Esses segmentos podem formar um triangulo!')
    if r1 == r2 == r3:
        print('Equilátero') #  se todos os lados iguais
    elif r1!= r2!= r3!= r1:
        print('Escaleno') # dois lado com mesma medida
    else:
        print('Isoceles') # lados diferentes
else:
    print('Esses segmentos não formam um triangulo')


