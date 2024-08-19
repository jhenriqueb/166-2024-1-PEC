def valida():

    print("Por favor, digite uma nota entre 0 e 10:")

    while True:
        try:
            nota = float(input())
            if 0 <= nota <= 10:
                return nota
            else:
                print('Nota inválida. A nota deve estar entre 0 e 10.')
        except ValueError:
            print('Nota inválida. Por favor, digite um número válido.')

def conceito(nota):

    if nota >= 8.5:
        return "A"
    elif nota >= 7.0:
        return "B"
    elif nota >= 5.0:
        return "C"
    elif nota >= 4.0:
        return "D"
    else:
        return "E"
    
def main():

    print("Bem-vindo ao sistema de conceitos!")
    nota = valida()
    resultado = conceito(nota)
    
    print(f"Seu conceito é: {resultado}")

if __name__ == '__main__':
    main()
