
print('')
n = str(input('Diga seu nome completo: ').strip())
nome = n.split() 
print('Prazer baranga'.upper())
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
