vendas = 1500
meta = 1300

if vendas > meta:
    print('Venderdor ganha bônus')
    print('Bateu a meta de vendas')
    bonus = 0.1 * vendas
    print('Bonus do vendedor:',bonus)
else:
    print('Vendedor não ganhou bonus')
    print('Não bateu a meta de vendas')

print('Acabou o Programa')

vendas = 1900
meta1 = 1300
meta2 = 2000

if vendas >= 2000:
    bonus = 0.13 * vendas
elif vendas >= 1300:
    bonus = 0.1 * vendas
else:
    bonus = 0

print('Bonus:', bonus)

lista_de_produto = ['popo', 'pão', 'caderno', 'copo']
produto_procurado = input('Procure um produto: ')
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_de_produto:
    print('produto no estoque')
else:
    print('não temos esse produto')


