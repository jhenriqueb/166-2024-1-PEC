def somatorio():
    soma = 0
    print("Digite uma quantidade indefinida de números inteiros positivos.")
    print("Digite 0 para encerrar a entrada e calcular a soma.")

    while True:
        try:
            n = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if n == 0:
            break

        if n > 0:
            soma += n
        else:
            print("Por favor, digite apenas números inteiros positivos.")
    
    return soma

def main():
    print("Bem-vindo ao somador de números!")
    resultado = somatorio()
    print(f'A soma dos números digitados é: {resultado}')

if __name__ == '__main__':
    main()
