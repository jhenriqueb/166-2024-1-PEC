def calcular(a,b,c):
    return 2 * a + 5 * b - c 

def main():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    z = int(input('Digite outro número: '))

    print(f'O resultado da expressão: {calcular(x, y, z )}')

if __name__ == '__main__':
    main()