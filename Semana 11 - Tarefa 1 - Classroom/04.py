def inverter(x):
  
    return int(str(x)[::-1])

def main():
    print("Bem-vindo ao programa de inversão de números!")
    print("Este programa inverte a ordem dos dígitos do número que você fornecer.")
    
    try:
        n = int(input("Digite um número inteiro para inverter: "))
        resultado = inverter(n)
        print(f'O número invertido é: {resultado}')
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

if __name__ == '__main__':
    main()
