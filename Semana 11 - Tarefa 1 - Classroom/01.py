def juros(x, y):
    acumulado = x
    anos = 0
    while acumulado < 2 * x:
        acumulado += acumulado * (y/100)
        anos += 1

    return anos

def main():
#Entrada
    deposito = float(input('Digite o deposito incial: '))
    taxa = float(input('Digite a taxa: '))

#Processo
    resultado = juros(deposito, taxa)

#Saída
    print(f'Em {resultado} anos')

if __name__ == '__main__':
    main()
