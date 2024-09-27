from random import randint
print ('Suas opções:')
print('''
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
print('')

computador = randint(0,2)
jogador = int(input('Qual sua jogada? '))
lista = ('PEDRA','PAPEL','TESOURA')

print('Jogada do usuario é {}'.format (lista[jogador])) 
print('computador escolheu {}'.format(lista[computador]))

if computador == 0:
    if jogador == 0:
        print('Deu empate')
    elif jogador == 1:
        print('computador perdeu')
    elif jogador == 2:
        print('computador ganhou')
    else:
        print('Jogada invalida')
elif computador == 1:
    if jogador == 0:
        print('computador ganhou')
    elif jogador == 1:
        print('deu empate')
    elif jogador == 2:
        print('computador perdeu')
    else:
        print('jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('computador perdeu')
    elif jogador == 1:
        print('computador ganha')
    elif jogador == 2:
        print('Deu empate')
    else:
        print('jogada invalida')
elif jogador >3:
    print('jogada inexistente')
print('')
