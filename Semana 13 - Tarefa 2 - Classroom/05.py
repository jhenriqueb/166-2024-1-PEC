def esta_ordenado(lista):

    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    print("Digite a quantidade de valores na lista:")
    n = int(data[0])
    
    lista = []
    print(f"Digite {n} valores, um por linha:")
    
    for i in range(1, n + 1):
        item = data[i]
        try:
            if '.' in item:
                lista.append(float(item))
            else:
                lista.append(int(item))
        except ValueError:
            lista.append(item)  

    if esta_ordenado(lista):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")

if __name__ == "__main__":
    main()
