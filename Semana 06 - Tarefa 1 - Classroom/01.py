def contador(x):
    return(len(x))

def main():
    x = input('Digite uma frase: ')
    y = contador(x)

    print(f'A frase {x} tem {y} caracteres')

if __name__ == '__main__':
    main()
    