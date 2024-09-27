n1 = float(input('Diga a primria nota: '))
n2 = float(input('Diga a segunda nota: '))
me = (n1+n2)/2

if (n1 + n2)/2 <= 5:
    print('VOCÊ FOI REPROVADO')
    print('ESTUDE MUITO MAIS, E PARE DE JOGAR LOL')
    print(f'Sua primeira nota foi {n1} a segunda nota {n2} o resultado é')
    print((n1+n2)/2)

elif 7> me >=5:
    print('VOCÊ TA DE RECUPERAÇÃO')
    print('ESTUDE MAIS')
    print(f'Sua primeira nota foi {n1} a segunda nota {n2} o resultado é')
    print((n1+n2)/2)

else: 
    print('VOCÊ FOI APROVADO')
    print('PARABÉNS')
    print('Sua primeira nota foi {} a segunda nota {} O resultado é' .format(n1,n2))
    print((n1+n2)/2)
