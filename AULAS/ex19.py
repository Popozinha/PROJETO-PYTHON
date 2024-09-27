from random import choice
a = input('Digite aqui: ')
b = input('Digite aqui: ')
c = input('Digite aqui: ')
d = input('Digite aqui: ')

lista = [a,b,c,d]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')