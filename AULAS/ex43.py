from time import sleep

peso = float(input('SEU PESO: '))
altura = float(input('SUA ALTURA: '))

sleep(2)

imc = peso / (altura ** 2)

if imc  <= 18.5:
    print('Você está abaixo do peso')
elif imc >18.05 <=25:
    print('Peso ideal') 
elif imc >25 <=30:
    print('SOBREPESO')
elif imc >30 <=40:
    print('OBESO')
else:
    print('OBESIDADE MORBIDA')
