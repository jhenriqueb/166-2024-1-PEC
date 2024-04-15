def verificar(x,y):
    if x == y:
        return ('QUADRADO')
    else:
        p = (x*2)+(y*2)
        a = x*y
        return(f'{p:.0f} - {a:.0f}')


def main():
#Entrada
    base = float(input('Digite o valor correspondente a base:'))
    altura = float(input('Digite um valor correspondente a altura:'))

#Processo
    resultado = verificar(base,altura)

#Saída
    print(resultado)


if __name__ == '__main__':
    main()