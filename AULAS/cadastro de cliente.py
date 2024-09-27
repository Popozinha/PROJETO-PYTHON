print('Bem vindo')
print('Somos a casa popozinho, compre agora o seu popozinho')

nome = input(' Digite seu nome aqui: ')
nome = nome.lower()

aroba = '@'
email = input('Digite seu email aqui: ')
if  email in ['@hotmail.com', '@gmail.com', '@']:
    print('email valido')
else:
    print('email invalido')

print('Lembrando que tem que ser maior de idade, pra cuidar de um popozinho')
idade = int(input('Digite aqui sua idade: '))

if idade >= 18:
    print('Parabens você está autorizado à comprar seu popozinho')
else:
    print('infelizmente o Popozinho vai ficar pra proxima')
    print('Volte quando tiver mais idade')

print(' Escolha um de nossos melhores popozinhos')
lista_popos = {'Popozinho fofo': 20.000, 'Popozinho medroso': 13.000, 'Pozinho anão': 50.000, 'Pozinho avestruz': 100.000,'Pozinho calabreso': 150.000}

print(lista_popos)

bb = input('Escolha seu popozinho: ')

if bb in lista_popos:
    print('Seu popo foi comprado com exito')
else:
    print('Sua compra não foi efetuada')


