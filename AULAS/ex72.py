numero = ('zero', 'um', 'dois', 'tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
print('='*60)
print('{:^60}'.format('diga um numero de 0 a 20, e se quiser parar digite 999'))
print('='*60)
while True:
    user=int(input('diga um numero entre 0 e 20: '))
    if user == 999:
        break
    print('vc digitou o numero',{numero[user]}) 
print('fim')