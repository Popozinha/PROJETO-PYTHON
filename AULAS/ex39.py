from datetime import date

ano  = date.today().year 
nas = int(input('Diga o ano que você nasceu: '))
idade = ano - nas
print('Quem nasceu em {} tem {} anos'.format(nas,idade))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    t = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(t))
    print('Seu alistamento será em {}'.format(ano + t))
elif idade > 18:
    t = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(t))
    print('Seu alistamento foi em {}'.format(ano - t))

print('\033[33m Tenha um bom dia \033[m')



print(ano)

