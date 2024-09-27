

print('**--**'*10)

velo = float(input('Qual é a velocidade atual do seu carro agora: '))

if velo >80:
    print('Você ultrapassou o limite de velocidade que é de 80km/h')
    multa = (velo-80) * 7 
    print('Você foi multado R$', multa)
print('Tenha um bom dia, dirija com segurança!')

print('**--**'*10)