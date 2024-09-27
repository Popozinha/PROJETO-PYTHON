produtos = ('pão', 2, 
            'carne', 45,
            'macarrão', 12 ,
            'feijão', 21,
            'cebola', 1.30,
            'beterraba', 2.49,
            'café', 4.50,
            'leite', 13,
            'bolacha', 5)
print('-'*30)
print(f'{'LISTA DE PREÇOS':^30}')
print('-'*30)
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<15}R$',end='')
    else:
        print(f'{produtos[pos]:>7.2f}')
print('-'*30)
'''print(f'carioca',
    'suina',
    'parafuso',
    'preto','pardo',
    'roxa','vermelha'
    'azul', 'amarela'
    'torrado', 'forte'
    'integral','instantaneo'
    'salgada', 'doce')'''