def e_vogal(caractere):
    if caractere.lower() in {'a', 'e', 'i', 'o', 'u'}:
        return True
    else:
        return False

def main():
    caractere = input('Digite a vogal: ')

    resultado = e_vogal(caractere)
    print(f'O caractere é: {resultado}')

if __name__ == '__main__':
    main()