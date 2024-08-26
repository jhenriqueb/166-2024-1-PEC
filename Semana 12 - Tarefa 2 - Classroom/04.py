def primo(x):
    if x <= 1:
        return False
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
        
    return True

def main():
    print("Bem-vindo ao verificador de números primos!")
    print("Por favor, insira um número inteiro para verificar se é primo:")
    
    try:
        numero = int(input().strip())
        
        if primo(numero):
            print(f"O número {numero} é primo.")
        else:
            print(f"O número {numero} não é primo.")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == '__main__':
    main()
