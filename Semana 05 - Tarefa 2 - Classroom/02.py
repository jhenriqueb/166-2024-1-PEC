def is_letra(caractere):
    letras = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return caractere in letras


caractere = input('Digite uma letra: ')

resultado = is_letra(caractere)
print(f'A caractere é: {resultado}')