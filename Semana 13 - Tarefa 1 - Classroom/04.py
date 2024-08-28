def armazenar():
    numeros = []
    impar = []
    par = []

    print("Por favor, insira 20 números inteiros:")
    for i in range(1, 21):
        while True:
            try:
                n = int(input(f"Digite o número {i}: "))
                numeros.append(n)
                if n % 2 == 0:
                    par.append(n)
                else:
                    impar.append(n)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")

    return numeros, impar, par

def main():
    print("Bem-vindo ao programa de armazenamento e classificação de números!")
    
    numeros, impar, par = armazenar()

    print("\nLista completa de números inseridos:")
    print(numeros)
    
    print("\nNúmeros pares:")
    print(par)
    
    print("\nNúmeros ímpares:")
    print(impar)

if __name__ == '__main__':
    main()
