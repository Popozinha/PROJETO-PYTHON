soma = c=0
while True:
    n = int(input('Diga um numero [999 para parar]: '))
    if n == 999:
        break
    soma += n
    c+=1
print(f'a soma é {soma} e a quantidade é {c}')

