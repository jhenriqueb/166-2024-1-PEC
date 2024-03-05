h = int(input('Quantas horas se passaram depois da meia noite: ').strip())
m = int(input('Quantos minutos se passram depois da meia noite: ').strip())
s = int(input('Quantos segundos se passaram depois da meia noite: ').strip())

passou_h = (h * 60) * 60
passou_m = (m * 60)
passou_total = passou_h + passou_m + s

print(f'Se passaram no total {passou_total} segundos após a meia noite')