def processar_lista(lista):

    lista_ordenada = sorted(lista)
    lista_processada = [
        x * 3 if i % 2 == 0 else x * 5
        for i, x in enumerate(lista_ordenada)
    ]
    return lista_processada

def main():
    lista_numeros = []
    
    print("Por favor, insira 100 números inteiros:")
    
    while len(lista_numeros) < 100:
        try:
            numero = int(input())
            lista_numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    print("Ordenando e processando os números...")

    lista_resultado = processar_lista(lista_numeros)
    
    print("Lista resultante após ordenação e processamento:")
    print(lista_resultado)

if __name__ == "__main__":
    main()
