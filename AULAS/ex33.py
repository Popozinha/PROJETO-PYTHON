print('')
a = int(input('primeiro numero: '))
b = int(input('segundo numero: '))
c = int(input('Terceiro numero: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior= b
if c>b and c>a:
    maior = c
print('')
print('O menor numero é ',menor)

print('O maior numero é ',maior)
print('')

