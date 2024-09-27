lista_vendas = [1000, 500, 1500, 800, 2000, 2300]
bonus_procurado  = input('Coloque aqui sua meta do mês: ')


meta_mes = 1200
percentual_bonus = 0.1
bonus_procurado = lista_vendas * percentual_bonus

for venda in lista_vendas:
    if bonus_procurado >= meta_mes:
       bonus = percentual_bonus * venda
    else:
        bonus = 0
    print(bonus)


for venda in lista_vendas:
    
    if venda >= meta_mes:
        bonus = percentual_bonus* venda
    else:
        bonus = 0
    print(bonus)
    