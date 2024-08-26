def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primos_no_intervalo(x, y):
    primos = []
    for num in range(x, y + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

def main():
    print("Bem-vindo ao programa de identificação de números primos!")
    print("Por favor, insira dois números inteiros para definir o intervalo.")
    print("O primeiro número deve ser menor ou igual ao segundo número.")
    
    try:
        x = int(input("Insira o valor de x: ").strip())
        y = int(input("Insira o valor de y: ").strip())
        
        if x > y:
            print("Erro: O valor de x deve ser menor ou igual ao valor de y. Por favor, tente novamente.")
        else:
            primos = primos_no_intervalo(x, y)
            if primos:
                print(f"Números primos entre {x} e {y}:")
                for primo in primos:
                    print(primo)
            else:
                print(f"Não há números primos entre {x} e {y}.")
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros válidos.")

if __name__ == "__main__":
    main()
