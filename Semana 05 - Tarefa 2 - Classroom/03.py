def is_consoante(caractere):
    consoantes = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    return caractere in consoantes


caractere = input('Digite uma consoante: ')

resultado = is_consoante(caractere)
print(f'O resultado é: {resultado}')
