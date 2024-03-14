def is_simbolo(caractere):
    simbolos = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    return caractere in simbolos


caractere = input('Digite um simbolo: ')

resultado = is_simbolo(caractere)
print(f'O resultado é: {resultado}')