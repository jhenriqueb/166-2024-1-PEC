def c_numerico(x):
   return(ord(x))

def main():
    x = input('Digite apenas um caractere: ')
    y = c_numerico(x)

    print(f'O caractere digitado {x} tem o código númerico {y}')

if __name__ == '__main__':
    main()