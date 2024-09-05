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

print("Digite 20 elementos para a lista A:")
lista_a = gerar_lista(tamanho_lista)

print("Digite 20 elementos para a lista B:")
lista_b = gerar_lista(tamanho_lista)

lista_c = somar_listas(lista_a, lista_b)

print("Lista A:", lista_a)
print("Lista B:", lista_b)

print("Lista C:", lista_c)
