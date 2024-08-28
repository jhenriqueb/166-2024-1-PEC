def multiplica_constante(lista, constante):
 
    return [x * constante for x in lista]

def main():
    lista_original = []
    
    print("Digite números inteiros (digite 0 para terminar):")
    while True:
        try:
            numero = int(input())
            if numero == 0:
                break
            lista_original.append(numero)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    try:
        constante = int(input("Digite o valor da constante: "))
    except ValueError:
        print("Por favor, insira um número inteiro válido para a constante.")
        return

    lista_multiplicada = multiplica_constante(lista_original, constante)
    print("Lista original:", lista_original)
    print("Lista multiplicada:", lista_multiplicada)

if __name__ == "__main__":
    main()
