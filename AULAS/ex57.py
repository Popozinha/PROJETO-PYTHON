
from time import sleep

print('-*-'*10)
print('       LOJA DE POZINHOS')
print('-*-'*10)
sleep(1)
print('Os melhores da comunidade, com melhores preços')
print('Temos uma incrivel variedade')
sleep(1)
print('')
nome = input('Diga seu nome: ')
print('nome {} registrado com sucesso'.format(nome))

sexo = input('Diga seu sexo: [M/F] ').strip().upper()[0]
while sexo not in 'MF':
        sexo = input('Dado invalido. informe novamente, qual seu sexo? ').strip().upper()[0]
print('Sexo {} registrado'.format(sexo))

idade = int(input('Diga sua idade: '))
while idade < 18:
    idade = int(input('Idade invalida, tente novamente: '))
print('cadastrado com sucesso')
sleep(1)


print('-*-'*10)


