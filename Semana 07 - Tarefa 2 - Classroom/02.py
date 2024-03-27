def contar_digitos_pares(numero):
    d1 = int(str(numero)[0])
    d2 = int(str(numero)[1])
    d3 = int(str(numero)[2])

    digitos_pares = (d1 % 2 == 0) + (d2 % 2 == 0) + (d3 % 2 == 0)
    
    return digitos_pares

def main():
    numero = int(input('Digite um número entre 100 - 999: '))
    
    if 100 <= numero <= 999:
        resultado = contar_digitos_pares(numero)
        print(f'Nesse número tem {resultado} algorimos pares')
    else:
        print('Número inválido')

if __name__ == "__main__":
    main()
