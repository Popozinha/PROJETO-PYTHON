frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso =''

for letra in range(len(junto) -1,-1,-1): 
    inverso += junto[letra]
print (f'O inverso de {junto} é {inverso}')
if inverso == junto:

    print('ele é um palindromo')
else:
    print('ele não é um palindromo')

# o primeiro -1 é de onde começa a ultima letra (como ele ta negativo vem de tras pra frente na variavel junto)
# o segundo -1 é ate onde vai do começo ao final porque o primeiro -1 ja esta colocando a ordem da frase de tras pra frente
# terceiro -1  é pra não pular letras, e contar normalmente de 1 em 1
