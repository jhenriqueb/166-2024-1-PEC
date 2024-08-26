def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    while len(sequencia) < n:
        sequencia.append(a)
        a, b = b, a + b
    
    return sequencia

def main():
    print("Bem-vindo ao gerador de sequência de Fibonacci!")
    print("Por favor, insira o número de termos desejado (deve ser maior que 2):")
    
    try:
        n = int(input().strip())
        
        if n >= 2:
            fib_sequencia = fibonacci(n)

            print(f"Sequência de Fibonacci com {n} termos:")
            print(', '.join(map(str, fib_sequencia)))
        
        else:
            print("O valor n deve ser maior que 2. Por favor, tente novamente.")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == '__main__':
    main()
