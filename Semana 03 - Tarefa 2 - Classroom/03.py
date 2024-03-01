dividendo = float(input('Digite o valor do dividendo: '))
divisor = float(input('Digite o valor do divisor: '))

resultado_divisao = dividendo // divisor
resto_divisao = dividendo % divisor

print(f'O resultado: {resultado_divisao:.4f}')
print(f'O resto: {resto_divisao:.4f}')