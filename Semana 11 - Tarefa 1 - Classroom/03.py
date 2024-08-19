def comparacao():
    maior = None
    menor = None

    print("Digite uma quantidade indefinida de números inteiros positivos. Digite 0 para encerrar a entrada.")

    while True:
        try:
            n = int(input("Digite um número inteiro positivo: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if n == 0:
            break

        if maior is None or n > maior:
            maior = n

        if menor is None or n < menor:
            menor = n

    return maior, menor

def main():
    maior, menor = comparacao()

    if maior is not None and menor is not None:
        print(f'O maior número digitado é: {maior}')
        print(f'O menor número digitado é: {menor}')
    elif maior is None and menor is None:
        print("Nenhum número positivo foi digitado.")
    else:
        print("Houve um erro na comparação dos números.")

if __name__ == '__main__':
    main()
