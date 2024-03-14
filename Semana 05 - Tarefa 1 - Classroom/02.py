def calcular_area(lado):
    return lado ** 2 

def calcular_perimetro(lado):
    return 4 * lado

def main():
    lado = float(input('Digite o lado do quadrado: '))

    area = calcular_area(lado)
    perimetro = calcular_perimetro(lado)

    print(f'Área do Quadrado: {area:>10.4f}')
    print(f'Perimetro do Quadrado: {perimetro:>10.4f}')

if __name__ == '__main__':
    main()