soma = 0
count = 0
for c in range (1,7):
    num = int(input('digite um valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        count = count + 1
print ('voce informou {} numeros PARES e asoma foi {}'.format(count,soma))