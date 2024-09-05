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

lista = ler_lista()
valor_pesquisado = int(input())
ocorrencias = count(lista, valor_pesquisado)

print(lista)
print(valor_pesquisado)
print(ocorrencias)
