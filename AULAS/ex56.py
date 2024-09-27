somaid = 0
mediaid = 0
homvelho = 0
nomevelho = ''
totmulher = 0
for c in range(1,5):
    print('')
    print('--- {}ª PESSOA ---'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaid += idade
    if c == 1 and sexo in 'Mm':
        homvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade> homvelho:
        homvelho = idade
        nomevelho = nome 
    if sexo in 'fF' and idade <20:
        totmulher += +1
    
mediaid = somaid /4
print('A media de idade do grupo é {}'.format(mediaid))
print('O nome do homem mais velho é {} e a idade é {}'.format(nomevelho, homvelho))
print('Mulheres com menos de 20 anos {} '.format(totmulher))






