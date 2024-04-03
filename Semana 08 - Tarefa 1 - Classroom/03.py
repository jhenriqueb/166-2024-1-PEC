def encontrar_maior_menor(n1, n2, n3, n4, n5):
    maior = n1
    menor = n1
    
    if n2 > maior:
        maior = n2
    elif n2 < menor:
        menor = n2

    if n3 > maior:
        maior = n3
    elif n3 < menor:
        menor = n3

    if n4 > maior:
        maior = n4
    elif n4 < menor:
        menor = n4

    if n5 > maior:
        maior = n5
    elif n5 < menor:
        menor = n5

    return maior, menor

def main():
    n1 = int(input('Digite o 1° número:'))
    n2 = int(input('Digite o 2° número:'))
    n3 = int(input('Digite o 3° número:'))
    n4 = int(input('Digite o 4° número:'))
    n5 = int(input('Digite o 5° número:'))

    maior, menor = encontrar_maior_menor(n1, n2, n3, n4, n5)

    print(f'O maior número: {maior}')
    print(f'O menor número: {menor}')

if __name__ == "__main__":
    main()
