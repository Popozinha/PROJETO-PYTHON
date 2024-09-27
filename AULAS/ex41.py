from datetime import date

print('')
atual = date.today().year
nas= int(input('DIGA SUA DATA DE NASCIMENTO: '))
idade =  atual - nas
print(' O atleta tem ',idade)

if idade <=9:
    print('VOCÊ É MIRIM')
elif  idade <=14:
    print(' VOCÊ É INFANTIL')
elif idade <=19:
    print(' VOCÊ É JÚNIOR')
elif  idade <=25:
    print('VOCÊ É SÊNIOR')
else:
    print('VOCÊ É MASTER')
