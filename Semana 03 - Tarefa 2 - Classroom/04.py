minutos = int(input('Digite o número de minutos: '))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f'{horas}h{minutos_restantes}min')