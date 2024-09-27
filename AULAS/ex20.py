import random

print('')
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')

lista = [ a,b,c,d ]
ordem = random.shuffle(lista)
print(f'A ordem de alunos são',lista)
print('')