def zero(x):
    lista = [0] * x
    print(f'\nLista com {x} zeros:')
    print(f'{lista}')
    return lista

def sequencia(x):
    lista = list(range(1, x + 1))
    print(f'\nLista com sequência de números de 1 a {x}:')
    print(f'{lista}')
    return lista

def teclado(x):
    lista = []
    print(f'\nDigite {x} números inteiros para criar a lista:')
    for i in range(x):
        while True:
            try:
                valor = int(input(f'Número {i + 1}: '))
                lista.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    print(f'\nLista com os números digitados:')
    print(f'{lista}')
    return lista

def invertido(x):
    lista = []
    print(f'\nDigite {x} números inteiros para criar a lista (os números serão inseridos na ordem inversa):')
    for i in range(x):
        while True:
            try:
                valor = int(input(f'Número {i + 1}: '))
                lista.insert(0, valor)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    print(f'\nLista com os números digitados na ordem inversa:')
    print(f'{lista}')
    return lista

def main():
    print("Bem-vindo ao programa de listas!")
    while True:
        try:
            n = int(input('\nDigite o número de elementos para as listas: '))
            if n <= 0:
                print("Por favor, insira um número inteiro positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro positivo.")
    
    zero(n)
    sequencia(n)
    teclado(n)
    invertido(n)

if __name__ == '__main__':
    main()
