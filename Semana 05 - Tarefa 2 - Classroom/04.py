def e_letra_ou_digito(caractere):
    letras_e_digitos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return caractere in letras_e_digitos

caractere = input('Digite uma letra e um número: ')

resultado = e_letra_ou_digito(caractere)
print(f'O resultado é: {resultado}')