ponto = int(input('PRIMEIRO TERMO:  '))# ONDE COMEÇA
razão = int(input('RAZÃO: ')) #QUANTAS CASAS PULA
p = ponto + (10 - 1) * razão

for c in range(ponto, p + razão , razão):
    print(c,end=' -> ')

print('ACABOU')
print(' ')  