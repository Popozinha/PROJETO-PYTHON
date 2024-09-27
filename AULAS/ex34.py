print('')
print('_8_8_'*10)
valor = float(input('Diga o seu salario: '))
if valor > 1250:
    conta= valor * 0.10
    print(f'Seu salario sofreu alteração de 10% ficando de aumento R${conta:.2f}')
    print(f'Seu salario atual é de {valor+conta}')

else:
    cont = valor * 0.15
    print(f'seu salario sofreu alteração de 15% ficando de aumento R${cont:.2f}') 
    print(f'Seu salario atual é {valor+cont}')  

print('')
print('Tenha um bom dia')
print('_8_8_'*10)
print('')