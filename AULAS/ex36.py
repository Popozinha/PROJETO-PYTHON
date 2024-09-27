diga = float(input('nos diga o valor da casa para ver se pode fiananciar: '))
salario = int(input('Diga seu salario: R$'))
anos = int(input('Em quantos anos quer pagar a casa: '))
prestação = diga / (anos*12)
minimo = prestação * 30/100
print(f' Voce consegue pagar a casa de {diga} com salario de {salario} em {anos} anos')
print (f'Por mês vc vai pagar {prestação:.2f}')

if prestação <= minimo:
    print('saldo ACEITO')
    print('Parabens pela sua compra')
    print('Tenha um bom dia')
    print('_8_8_'*10)
    print('')
else:
    print('saldo NAO ACEITO')
    print('Infelizmente voce nao pode comprar a casa')
    print('Tenha um bom dia')
    print('_8_8_'*10)
    print('')