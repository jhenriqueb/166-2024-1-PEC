def ler_lista(tamanho):
    lista = []
    print(f"Por favor, insira {tamanho} números inteiros para a lista:")
    for i in range(1, tamanho + 1):
        while True:
            try:
                numero = int(input(f"Digite o número {i}: "))
                lista.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    return lista

def intercala_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada

def main():
    tamanho_lista = 25
    print("Bem-vindo ao programa de intercalamento de listas!")
    
    print(f"\nCriando a primeira lista com {tamanho_lista} números:")
    A = ler_lista(tamanho_lista)

    print(f"\nCriando a segunda lista com {tamanho_lista} números:")
    B = ler_lista(tamanho_lista)

    C = intercala_listas(A, B)

    print("\nPrimeira lista:")
    print(A)
    print("\nSegunda lista:")
    print(B)
    print("\nLista intercalada:")
    print(C)

if __name__ == "__main__":
    main()
