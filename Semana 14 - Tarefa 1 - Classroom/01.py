def ler_lista():
    lista = []
    while True:
        valor = int(input("Digite um número (0 para terminar): "))
        if valor == 0:
            break
        lista.append(valor)
    return lista

def comprimento(lista):
    count = 0
    for item in lista:
        count += 1
    return count

def inverter(lista):
    lista_invertida = []
    for i in range(comprimento(lista)):
        lista_invertida.append(lista[comprimento(lista) - 1 - i])
    return lista_invertida

def minimo(lista):
    if comprimento(lista) == 0:
        return None
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

def maximo(lista):
    if comprimento(lista) == 0:
        return None
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

def soma(lista):
    total = 0
    for item in lista:
        total += item
    return total

lista = ler_lista()

print("Lista:", lista)
print("Comprimento da lista:", comprimento(lista))
print("Lista invertida:", inverter(lista))
print("Menor valor da lista:", minimo(lista))
print("Maior valor da lista:", maximo(lista))
print("Soma dos valores da lista:", soma(lista))
