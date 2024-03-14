def inverter_numero(numero):
    return int(str(numero)[::-1])

def main():
    numero = int(input('Digite os números para serem invertidos: '))
    
    numero_invertido = inverter_numero(numero)

    print(f'O número {numero} invertido fica: {numero_invertido}')

if __name__ == '__main__':
    main()