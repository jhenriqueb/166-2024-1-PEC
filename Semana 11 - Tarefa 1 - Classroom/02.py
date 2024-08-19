def aritmetica():
    soma = 0
    contagem = 0

    while True:
        n = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))

        if n == 0:
            break

        if n > 0:
            soma += n
            contagem += 1

    if contagem > 0:
        media = soma / contagem
        return media
    else:
        return None

def main():
    media = aritmetica()
    if media is not None:
        print(f'A média aritmética dos números digitados é: {media:.2f}')
    else:
        print("Nenhum número positivo foi digitado.")

if __name__ == '__main__':
    main()
