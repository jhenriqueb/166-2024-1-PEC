def ler_numeros():
    numeros = []
    print("Por favor, insira 10 números inteiros:")
    for i in range(10):
        while True:
            try:
                numero = int(input(f"Digite o número {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    return numeros

def calcular_soma_produto(numeros):
    soma = sum(numeros)
    produto = 1
    for numero in numeros:
        produto *= numero
    return soma, produto

def main():
    numeros = ler_numeros()
    soma, produto = calcular_soma_produto(numeros)

    print("\nNúmeros inseridos:")
    print(numeros)
    print(f"\nSoma dos números: {soma}")
    print(f"Produto dos números: {produto}")

if __name__ == "__main__":
    main()
