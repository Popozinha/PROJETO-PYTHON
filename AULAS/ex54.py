from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range (1,8):
    pessoa = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano - pessoa
    if idade >=21:
        maior+= +1
    else:
        menor+= +1
print('Ao todo tivemos {} maiores de idade'.format(maior))
print('tivemos {} menores de idade'.format(menor))