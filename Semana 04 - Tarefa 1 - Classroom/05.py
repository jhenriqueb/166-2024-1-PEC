altura = int(input('Digite a altura:'))
largura = int(input('Digite a largura: '))
comprimento = int(input('Digite o comprimento: '))

area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_paredes = 2 * altura * largura + 2 * altura * comprimento

print(f'Área do piso: {area_piso}')
print(f'Volume da sala: {volume_sala}')
print(f'Área das paredes: {area_paredes}')