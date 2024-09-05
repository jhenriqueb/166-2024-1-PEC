def ler_lista():
    lista = []
    while True:
        valor = int(input())
        if valor == 0:
            break
        lista.append(valor)
    return lista

def count(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

print("Digite os elementos da lista (0 para terminar):")
lista = ler_lista()

valor_pesquisado = int(input("Digite o valor a ser pesquisado: "))

ocorrencias = count(lista, valor_pesquisado)
print("Lista:", lista)
print("Valor pesquisado:", valor_pesquisado)
print("Número de ocorrências:", ocorrencias)
