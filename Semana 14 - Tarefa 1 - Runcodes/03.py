def gerar_lista(tamanho):
    lista = []
    for _ in range(tamanho):
        elemento = int(input())
        lista.append(elemento)
    return lista

def somar_listas(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

tamanho_lista = 20

lista_a = gerar_lista(tamanho_lista)
lista_b = gerar_lista(tamanho_lista)
lista_c = somar_listas(lista_a, lista_b)

print(lista_a)
print(lista_b)
print(lista_c)
    