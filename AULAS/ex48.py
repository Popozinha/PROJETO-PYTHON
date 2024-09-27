soma = 0
cout = 0
for c in range( 1 , 500 , 2):
    if c % 3 == 0:
        soma = soma + c
        cout = cout + 1
print ('o resultado dos {} deu {}'.format(cout, soma))



   