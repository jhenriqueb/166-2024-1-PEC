def valor(x):
    if x % 2 != 0:
        return(True)
    else:
        return(False)
    
def main():
    x = int(input('Digite um valor para saber se é impar(False) ou par(True): '))
    
    res = valor(x)

    print(f'O número é {res}')

if __name__ == '__main__':
    main()