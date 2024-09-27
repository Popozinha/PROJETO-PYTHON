menor = 0
maior = 0
for p in range (1,6):
    peso = float(input('Digite o peso {}ª pessoa: '. format (p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso >maior:
            maior = peso
        if peso < menor:
            menor = peso
print('')
print('O maior peso lido foi {} Kg'.format(maior))
print('O menor peso lido foi {} Kg'.format(menor))