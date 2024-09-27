'''print('tar_tar_tar')
print('')

p = input('Digite algo: ')
print (type(p))

n = input('Digite algo: ')
class bool:
    print (n.isalnum())

m = input('Digite algo: ')

class bool:
    print (m.isalpha())

o = input('Digite algo: ')
class bool:
    print (o.islower())

n1 = int(input('digite algo: '))
n2 = int(input('digite algo: '))
n = n1 + n2
print(f'{n1} {n2}',n )

n1 = int(input('digite algo: '))
n2 = int(input('digite algo: '))'''

'''somaidade= 0
mediaidade = 0
nomehomi = ''
idadeunisex = 0
totmule = 0
tothomi = 0
for c in range (1,4):
    print('--- {}ª PESSOA ---'.format(c))
    nome = input('NOME: ').strip()
    idade = int(input('IDADE: '))
    sexo = input('SEXO [F/M]: ').strip()
    somaidade += idade
    if c==1 and sexo in 'mM':
        idadeunisex= idade
        nomehomi = nome
    if sexo in 'Mm' and idade >idadeunisex:
        idadeunisex= idade
        nomehomi = nome
    if sexo in 'fF' and idade < 20:
        totmule += +1
    if sexo in 'Mm':
        tothomi += +1
    if sexo in 'fF' and idade > idadeunisex:
        idadeunisex = idade
    
mediaidade = somaidade / 3
print('MEDIA DE IDADE DO GRUPO É {:.2f}'.format(mediaidade))
print('O NOME DO HOMEM MAIS VELHO É {} E A SUA IDADE É {}'.format(nomehomi,idadeunisex))
print('TEMOS UM TOTAL DE {} COM MENOS DE 20 ANOS'.format(totmule))
print('TEMOS UM TOTAL DE {} HOMENS'.format(tothomi))
print('TEMOS TAMBEM MULHERES MAIORES DE IDADE COM {}'.format(idadeunisex))
'''
from random import choice

fruta= choice('banana', 'pera', ' jaca')

print(fruta)










