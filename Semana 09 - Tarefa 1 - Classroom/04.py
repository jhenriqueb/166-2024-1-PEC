def determinar(x,y,z):
    seg = abs(x - y)
    ter = abs(x - z)
    if seg < ter:
        return seg
    else:
        return ter


def main():
#Entrada
    n1 = int(input('Digite o primeiro numero:'))
    n2 = int(input('Digite o segundo numero:'))
    n3 = int(input('Digite o terceiro numero:'))

#Processo
    resultado = determinar(n1,n2,n3)

#Saída
    print('A menor diferença com relaçao ao primeiro numero é:',resultado)


if __name__ == '__main__':
    main()