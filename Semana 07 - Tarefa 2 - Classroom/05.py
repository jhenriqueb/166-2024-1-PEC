def ordenar_numeros(a, b, c):
    if a <= b <= c:
        return a, b, c
    elif a <= c <= b:
        return a, c, b
    elif b <= a <= c:
        return b, a, c
    elif b <= c <= a:
        return b, c, a
    elif c <= a <= b:
        return c, a, b
    else:
        return c, b, a

def main():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite o segundo número: '))
    num3 = int(input('Digite o terceriro número:'))

    menor, meio, maior = ordenar_numeros(num1, num2, num3)
    
    print(menor)
    print(meio)
    print(maior)
    
if __name__ == "__main__":
    main()
