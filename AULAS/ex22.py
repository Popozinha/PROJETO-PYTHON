print('')
nome = str(input('Diga seu nome completo: ')).strip()
print('O seu nome maiusculo é {}'.format(nome.upper()))
print(f'O seu nome minusculo é {nome.lower()}')

print('o seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('')
