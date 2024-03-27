def verificar_digitos_impares(numero):
    d1 = numero // 10
    d2 = numero % 10
    
    if d1 % 2 == 0 and d2 % 2 == 0:
        return "Nenhum dígito é ímpar."
    elif d1 % 2 != 0 and d2 % 2 != 0:
        return "Os dois dígitos são ímpares."
    else:
        return "Apenas um dígito é ímpar."

def main():
    numero = int(input('Digite um número entre 10-99: '))
    
    if 10 <= numero <= 99:
        resultado = verificar_digitos_impares(numero)
        print(resultado)
    else:
        print('Número inválido')

if __name__ == "__main__":
    main()
