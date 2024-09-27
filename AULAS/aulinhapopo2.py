lista = [{'biscoito':12, 'chilito':9, 'guarana':2, 'arroz':15, 'pirulito':5, 'jujuba':23, 'chocolate':44, 'coca':14, 'caixa de bombom':64}]
mercado = input('Diga oque quer comprar: ')
m = mercado.lower

if mercado in lista:
    print(' O produto desejado tem no estoque')
else:
    print('O produto desejado não tem no estoque')

#lista = int([{'biscoito':12, 'chilito':9, 'guarana':2, 'arroz':15, 'pirulito':5, 'jujuba':23, 'chocolate':44, 'coca':14, 'caixa de bombom':64}])
#print(n)