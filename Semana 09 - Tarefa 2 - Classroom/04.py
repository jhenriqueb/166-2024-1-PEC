def calcular(x,y):
    p1 = 2.50 if x <= 5 else 2.20
    p2 = 1.80 if y <= 5 else 1.50

    total = (x*p1)+(y*p2)

    if x + y > 8 or total > 25.00:
        total *= 0.9

    return total


def main():
#Entrada
    morango = float(input('Digite a quantidade de morangos em kg:'))
    maca = float(input('Digite a quantidade de maças em kg:'))

#Processo
    valor = calcular(morango,maca)

#Saída
    print(f'O valor a ser pago será {valor:.2f}')


if __name__ == '__main__':
    main()