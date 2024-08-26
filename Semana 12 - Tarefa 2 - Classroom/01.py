def fatorial(x):

    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)

def main():
    print("Bem-vindo ao calculador de fatorial!")
    print("Por favor, insira um número inteiro não negativo para calcular o fatorial:")
    
    try:
        numero = int(input().strip())
        
        if numero < 0:
            print("Por favor, insira um número inteiro não negativo.")
            return

        resultado = fatorial(numero)
        
        print(f"O fatorial de {numero} é {resultado}.")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == '__main__':
    main()
