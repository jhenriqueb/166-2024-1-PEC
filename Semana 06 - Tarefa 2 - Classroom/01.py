def contar_caracteres(frase):
    frase = frase.strip()
    num_caracteres = len(frase)
    return num_caracteres

def main():
    frase = input('Digite uma frase: ')
    num_caracteres = contar_caracteres(frase)
    print("Número de caracteres na frase:", num_caracteres)

if __name__ == "__main__":
    main()