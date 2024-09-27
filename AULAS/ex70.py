total= mais= menor = c=0
barato =''
print('°'*30)
print('     LOJA SUPER POZINHO')
print('°'*30)
while True:
    p = str(input('nome do produto: ')).strip().upper()
    prço= float(input('preço do produto: R$ '))
    c+=1
    escolha = ' '
    if c == 1 or prço < menor:
        menor = prço
        barato= p

    total+= prço
    if prço > 1000:
        mais+=1
    while escolha not in 'SN':
        escolha = input('quer continuar[S|N]: ').strip().upper()
    print('°'*30)    
    if escolha == 'N':
        break
    
print(f'total das compras deu R$ {total}')
print(f'temos {mais} produto custando mais de R$ 1000,00 reais ')
print(f'o produto mais barato foi {barato} e custa: R$ {menor}')
print('')