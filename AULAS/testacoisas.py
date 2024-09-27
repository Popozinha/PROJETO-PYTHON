'''from time import sleep
r1 = (input('DIGA SEU NOME: '))
r2 = int(input('DIGA SUA IDADE: '))
r3 = (input('DIGA O NOME DA SUA NAMORADA: '))

sleep(2)

if r1 == 'Popozinho':
    print('\033[32m QUE BELO NOME! \033[m')
    if r3 == 'Popozinha':
        print('\033[35m Huuu! BELA ESCOLHA \033[m')
if r2 == 28:
    print('\033[34m SUA POPOZINHA VAI FAZER UMA SURPRESINHA\033[m')
if r3 == 'Popozinha':
    print('\033[33m SUA POPOZINHA AMA MUUUUITO \033[m')
else:
    print('\033[31m VOCÊ NÃO É QUEM EU PROCURO, DA O FORA\033[m')'''


'''con = 0
n = int(input('Digite um numero: '))
print('')
for c in range(1 ,n +1):
    if n %c == 0:
        print('\033[34m ', end=' ')
        print('{}'.format(c), end=' -> ')
        con += 1
    else:
        print('\033[32m ', end=' ')
        print('{}'.format(c), end=' -> ')
print('\033[36mACABOU!\033[m')
print('')       
print(f'\n\033[mO numero {n} foi divisivel {con} vezes')
if con == 2:
    print('o numero é Primo')
else:
    print('O numero não é primo')'''

'''maior = 0
menor = 0
for pessoa in range(1,6):
    peso =float(input('peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso 
        menor = peso
    else:
        if  peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa com maior peso é {}'.format(maior))
print('E {} a pessoa que tem menor peso '. format(menor))'''


'''mediaidade= 0
somaidade = 0
nomehome = ''
idadehome = 0
totalmule = 0
for c in range (1,3):
    print('--- {}ª PESSOA ---')
    nome = input('Seu nome: ')
    idade = int(input('Sua idade: '))
    sexo = input('sexo [F/M]: ')
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        idadehome = idade
        nomehome = nome
    if sexo in 'Mm' and idade> idadehome:
        idadehome = idade
        nomehome = nome
    if sexo in 'Ff' and idade <20:
        totalmule+= +1
    
mediaidade = somaidade /2
print('\033[43mmedia de idade {}\033[m'.format(mediaidade))
print('o nome do homem mais velho é {}'.format(nomehome))
print('Total de mule {}'.format(totalmule))'''


'''n = int(input('Primeiro termo: '))
r = int(input('Qual razão: '))
cont = 1
total = 10
mais = total    
while mais != 0:
    total+= mais 
    while cont <= total -10:
        print('{} -> '.format(n),end='')
        n+=r 
        cont+= 1 
    print('fim')
    mais=(int(input('Quantos termos a mais vc quer? ')))
print('fim')
'''

'''print('\033[35m´`\033[m'*20)
print('\033[34m        SEQUENCIA FIBONACCI\033[m')
print('\033[35m´`\033[m'*20)
n = int(input('\033[34mQUANTOS TERMOS VC UER MOSTRAR? \033[m'))
t1 = 0
t2 = 1
c = 3
t3 = t1 + t2
print('\033[32m{} -> {} ->\033[m'.format(t1,t2),end='')
while c <= n:
    t3=t1+t2
    print('\033[32m {} -> \033[m'.format(t3),end='')
    t1 = t2
    t2 = t3
    c+=1
print('\033[31mFIM\033[m')
print('')
'''
#TUPLAS SÃO IMUTAVEIS#
'''lanche = ('refrigerante','Hamburguer', 'suco', 'pizza', 'pudim', 'limonada','pera')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('comi pra caramba!')
'''
'''while True:
    user = input('Qual produto deseja acrecentar? ')
    preço = int(input('Quanto custa? '))
    print('\033[33m=\033[m'*30)
    print(f'\033[31m{'MAC LANCHE FELIZ':^30}\033[m')
    print('\033[33m=\033[m'*30)
    lanche = ('refrigerante', 5.3,
            'Hamburguer', 20,
            'suco', 4.40,
            'pizza', 12,
            'pudim', 9.50,
            'limonada', 6,
            'sorvete', 7.70)
    for comida in range(0,len(lanche)):
        if comida % 2 == 0:
            print(f'{lanche[comida]:.<20}R$',end='')
        else:
            print(f'{lanche[comida]:>7.2f}')
    lista = (f'refrigerante', 5.3,
                    'Hamburguer', 20,
                    'suco', 4.40,
                    'pizza', 12,
                    'pudim', 9.50,
                    'limonada', 6,
                    'sorvete', 7.70,
                    {user},{preço})
    for item in range(preço,user):
        if item % 2 == 0:
            print(f'{user[item]:.<20}R$',end='')
        else:
            print(f'{preço[item]:>5}R$',end='')
     
    print('\033[33mPA RA PA PA PA!\033[m')
    if user == 'fim':
        break
print('fim')
'''