def horas(x):
    return x//60

def min(x):
    return x%60 

def main():
    x = int(input('Digite os minutos: '))

    h = horas(x)
    m = min(x)

    print(f'{h}:{m}')

if __name__ == '__main__':
    main()