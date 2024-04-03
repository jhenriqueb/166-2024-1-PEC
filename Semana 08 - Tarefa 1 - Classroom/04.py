def calcular_media(*numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def main():
    numero1 = int(input('Digite o 1° número: '))
    numero2 = int(input('Digite o 2° número: '))
    numero3 = int(input('Digite o 3° número: '))
    numero4 = int(input('Digite o 4° número: '))
    numero5 = int(input('Digite o 5° número: '))

    media = calcular_media(numero1, numero2, numero3, numero4, numero5)

    print(f'A média dos números digitados é: {media:.2f}')

    print('Os números maiores do que a média: ')
    if numero1 > media:
        print("{:.2f}".format(numero1))
    if numero2 > media:
        print("{:.2f}".format(numero2))
    if numero3 > media:
        print("{:.2f}".format(numero3))
    if numero4 > media:
        print("{:.2f}".format(numero4))
    if numero5 > media:
        print("{:.2f}".format(numero5))

if __name__ == "__main__":
    main()
