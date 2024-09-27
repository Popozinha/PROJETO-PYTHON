roda = int(input('Diga a quantidade de dias: '))
k = int(input('Diga a quantidade de KM: '))
pista = (roda * 60) + (k * 0.15)
print(pista)

#atividade 14
c = float(input('digite graus em C°: '))
f = 9 * c / 5 + 32
print (' Os graus está em F°', f)

#atividade 13
print('')
bo = int(input('coloque seu salario: R$ '))
print('Vc terá uma adição de 15%')
novo_valor = bo - (bo * 15 / 100)
print(novo_valor)
print('')

salario = int(input('Digite seu salario para saber qual será sua adição de 15%: R$ '))
nos = salario * 15 /100
print('Sua adição será de', nos)
print(' ')
#atividade 12

nome = int(input('Diga a nós o preço desejado: '))
print(f'Coloque {nome} que deseja, e será adicionadao 5% de desconto: R$ ')
valor = nome - (nome * 10 / 100)
print (valor)
print('')

#atividade 1
n = (int(input('digite um numero: ')))
print(f'o antecessor do {n} é {n-1} e o sucessor é {n+1}')
print('')
#atividade 6
momo = int(input('digite um numero: '))
print(f'o dobro de {momo} é {momo*2},\no triplo de {momo} é {momo*3},\ne a raiz quadrada de {momo} é {momo**(1/2):.2f}')
print('')
#atividade 7
n1 = float(input('Primeira nota do aulo: '))
n2 = float(input('segunda nota do aluno: '))
print(f'A média entre {n1} e {n2} é igual á {(n1+n2)/2}')
print('')
#atividade 8
medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
m = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'O valor {medida} em mm {mm} em cm {cm} em dm {dm} em m {m} em dam {dam} em hm {hm} e em km {km}')
print('')
#atividade 9
print('')
num = int(input('Digite um numero: '))
print('-'*12)
print(f'{num} x {2} = {num*2}')
print(f'{num} x {3} = {num*3}')
print(f'{num} x {4} = {num*4}')
print(f'{num} x {5} = {num*5}')
print(f'{num} x {6} = {num*6}')
print(f'{num} x {7} = {num*7}')
print(f'{num} x {8} = {num*8}')
print(f'{num} x {9} = {num*9}')
print(f'{num} x {10} = {num*10}')
print('-'*12)
mo = int(input('Digite um numero: '))
print('-'*12)
print(f'{mo} - {1} = {mo-1}')
print(f'{mo} - {2} = {mo-2}')
print(f'{mo} - {3} = {mo-3}')
print(f'{mo} - {4} = {mo-4}')
print(f'{mo} - {5} = {mo-5}')
print(f'{mo} - {6} = {mo-6}')
print(f'{mo} - {7} = {mo-7}')
print(f'{mo} - {8} = {mo-8}')
print(f'{mo} - {9} = {mo-9}')
print(f'{mo} - {10} = {mo-10}')
print('-'*12)

#atividade 10
dinhe = float(input('Você tem quanto na carteira: R$ '))
dolar = dinhe / 5.15
print(f'Você consegue com R$ {dinhe} comprar U$ {dolar:.2f}')
print('')

#atividade 11
larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg*alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
tinta = area/2
print(f'para pintar sua parede, você precisa de {tinta}L de tinta.')
print('')




