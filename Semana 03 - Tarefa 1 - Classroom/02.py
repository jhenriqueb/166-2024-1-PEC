x = int(input('Digite a distância do planeta: '))
y = int(input('Digite a velocidade da nave: '))

z = x//y
print(f'{z//24} dias e {z%24} horas')