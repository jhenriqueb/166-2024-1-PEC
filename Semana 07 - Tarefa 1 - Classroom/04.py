def verificar_tipo_caractere(caractere):
    if caractere.isalpha():
        if caractere.lower() in 'aeiou':
            return "vogal"
        else:
            return "consoante"
    elif caractere.isdigit():
        return "número"
    else:
        return "símbolo"
    
def main():

    caractere = input('Digite um carectere: ')

    res = verificar_tipo_caractere(caractere)

    print(f'O valor do carectere {caractere} é {res}')
    
if __name__ == '__main__':
    main()