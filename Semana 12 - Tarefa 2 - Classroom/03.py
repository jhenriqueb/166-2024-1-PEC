def calcular(x):
    h = 0
    for i in range(1, x + 1):
        h += 1 / i
    return h

def main():
    print("Bem-vindo ao calculador da série harmônica!")
    print("Por favor, insira um número inteiro positivo para calcular a série harmônica até esse termo:")
    
    try:
        n = int(input().strip())
        
        if n > 0:
            valor = calcular(n)
            
            print(f"A soma da série harmônica até o termo {n} é: {valor:.4f}")
        
        else:
            print("O valor deve ser um número inteiro positivo. Por favor, tente novamente.")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == '__main__':
    main()
