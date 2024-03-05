a = int(input('Anos: '))
m = int(input('Mêses: '))
d = int(input('Dias: '))

anos = a * 365
mes = m * 30 
total = mes + anos + d

print(f'Total de dias: {total}')