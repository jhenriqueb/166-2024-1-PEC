def exibir():

    print("\nCÓDIGO  PRODUTO         PREÇO (R$)")
    print('H       Hamburger       5,50')
    print('C       Cheeseburger    6,80')
    print('M       Misto Quente    4,50')
    print('A       Americano       7,00')
    print('Q       Queijo Prato    4,00')
    print('X       PARA TOTAL DA CONTA')
    print("Digite o código do produto desejado ou 'X' para finalizar e obter o total.")

def calcular():

    menu = {
        'H': 5.50,
        'C': 6.80,
        'M': 4.50,
        'A': 7.00,
        'Q': 4.00
    }

    total = 0

    while True:
        exibir()
        codigo = input("Digite o código do produto: ").upper()[0]

        if codigo == "X":
            break

        elif codigo in menu:
            total += menu[codigo]
            print(f"Produto {codigo} adicionado ao total. Preço: R$ {menu[codigo]:.2f}")
        else:
            print("Opção inválida. Por favor, digite um código de produto válido ou 'X' para finalizar.")
    
    return total

def main():
    print("Bem-vindo ao sistema de pedidos!")
    resultado = calcular()
    print(f"\nO total da sua conta é: R$ {resultado:.2f}")

if __name__ == '__main__':
    main()
