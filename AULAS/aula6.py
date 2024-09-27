dic_produtos = {'pão': 2, 'salsicha': 10, 'milho': 4, 'carne muida': 20, 'ervilho':5}

print (dic_produtos['pão'])

dic_produtos ['pão']= dic_produtos ['pão'] * 2
dic_produtos ['milho']= dic_produtos ['milho'] * 3.3
dic_produtos['salsicha'] = dic_produtos['salsicha'] * 5
print(dic_produtos)

#quantidade de produtos
print(len(dic_produtos))

#retirar um item
##print(dic_produtos)

#coloca um item no dicionario
dic_produtos['pipoca'] = 3
print(dic_produtos)

dic_produtos['pipoca'] = int(dic_produtos['pipoca'] * 4.3)
print(dic_produtos)
print('faz o L')

#verificar se um intem existe no dicionario
if 'salsicha' in dic_produtos:
    print('Exixte produto')
else:
    print('Não existe')

#verificar se um valor existe nos valores do dicionario
if 50 in dic_produtos.values():
    print('Exixte valor')
else:
    print('Não existe')

#ativividade 1
nome_produto = input('Nome do produto: ')
preco_produto = input('Preço do produto: ')

nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

#atividade 2

for produto in dic_produtos:
   novo_preco = int(dic_produtos[produto] * 1.1)
   dic_produtos[produto] = novo_preco

print(dic_produtos)


