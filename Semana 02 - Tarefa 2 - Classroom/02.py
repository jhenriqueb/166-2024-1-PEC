x = int(input('Insira um número em horas: '))
ret = x * 3
cal = (x * 60) - ret

print(f'Retirando 3 min a cada {x} horas sobrará {cal} minutos')