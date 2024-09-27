preço = float(input('DIGA O VALOR DA COMPRA: R$ '))

print ('''FORMAS DE PAGAMENTO
       [1] Á VISTA DINHEIRO/CHEQUE
       [2] Á VISTA CARTÃO
       [3] 2X NO CARTÃO
       [4] 3X OU MAIS NO CARTÃO''')

opçaõ = int(input('QUAL SUA OPÇÃO: ')) 

if opçaõ == 1:
    o1 = preço - (preço * 10 /100) 
    print(f'Sua compra é com 10% de desconto foi {o1:.2f}')
elif opçaõ == 2:
    m2 = preço * 5 /100
    p = preço - m2
    print(f'Suas compras no cartão com 5% de desconto foi {p:.2f}')
elif opçaõ == 3:
    j = preço / 2
    print(f'suas compras foram de {preço} dividido em 2x no cartão ficando um preço de R$ {j} ')
elif opçaõ == 4:
    x = int(input('Quantas parcelas: '))
    if x >= 3:
        t = preço * 0.20 # juros
        pp = t + preço # produto om juros mais produto
        y = pp / x # produto com juros parcelado 
        print(f'Suas compras foram de 3x no cartão o valor da compra é {preço} com 20% de juros fica {pp}')
        print(f'parcelando em {x} fica {y:2f}')
    else:
        print('Opção inválida')
else:
    print('OPÇÃO INVÁLIDA')
    print('Tente novamente')
    print('')
    
         
         






