def soma_cumulativa(lista):

    cumulativa = []
    soma = 0
    for numero in lista:
        soma += numero
        cumulativa.append(soma)
    return cumulativa

def main():
    lista_original = []
    
    print("Digite uma quantidade indeterminada de números reais (digite 0 para encerrar):")
    
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == 0:
                break
            lista_original.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número real.")

    lista_cumulativa = soma_cumulativa(lista_original)
    
    print("Lista original:", lista_original)
    print("Lista com soma cumulativa:", lista_cumulativa)

if __name__ == "__main__":
    main()
