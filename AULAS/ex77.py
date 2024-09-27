palavras = ('comida','peixe','computador','cafe','telhado','papai','esmalte',
            'pente','escova','celular')
for c in palavras:
    print(f'\n* Na palavra \033[31m{c.upper()}\033[m temos   ',end='')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(f'\033[33m{letras}\033[m',end=' ')