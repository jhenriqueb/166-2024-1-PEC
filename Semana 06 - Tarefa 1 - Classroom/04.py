def maior(n1,n2,n3,n4,n5):
    return(max(n1,n2,n3,n4,n5))

def menor(n1,n2,n3,n4,n5):
    return(min(n1,n2,n3,n4,n5))

def media(n1,n2,n3,n4,n5):
    return((n1+n2+n3+n4+n5) / 5)


def main():
    numero1 = int(input('Digite o 1° número: '))
    numero2 = int(input('Digite o 2° número: '))
    numero3 = int(input('Digite o 3° número: '))
    numero4 = int(input('Digite o 4° número: '))
    numero5 = int(input('Digite o 5° número: '))

    maior_numero = maior(numero1, numero2, numero3, numero4, numero5)
    menor_numero = menor(numero1, numero2, numero3, numero4, numero5)
    media_a = media(numero1, numero2, numero3, numero4, numero5)

    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")
    print(f"Média dos números: {media_a}")

if __name__ == "__main__":
    main()