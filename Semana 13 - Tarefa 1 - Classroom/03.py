def reais(x):
    lista = []
    if x == 0:
        print("\nLista vazia: []")
    else:
        print(f"\nDigite {x} números reais:")
        for i in range(x):
            while True:
                try:
                    valor = float(input(f'Número {i + 1}: '))
                    lista.append(valor)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número real.")
        
        inversos = [f'{valor}' for valor in reversed(lista)]
        print(f"\nLista com os números em ordem inversa:")
        print(f"[{', '.join(inversos)}]")

def escola(x):
    if x == 0:
        print("\nLista vazia: []")
        print("SEM NOTAS")
        return
    else:
        print(f"\nDigite {x} notas:")
        notas = []
        for i in range(x):
            while True:
                try:
                    nota = float(input(f'Nota {i + 1}: '))
                    notas.append(nota)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira uma nota válida.")

    media = sum(notas) / x
    formatada = [f'{nota:.1f}' for nota in notas]
    print(f"\nNotas inseridas:")
    print(f"[{', '.join(formatada)}]")
    print(f"Média das notas: {media:.1f}")

def letras(x):
    vogais = 'aeiouAEIOU'
    consoantes = []
    total = 0

    print(f"\nDigite {x} letras (uma por vez):")
    for i in range(x):
        letra = input(f'Letra {i + 1}: ')[0]
        if letra in vogais:
            total += 1
        elif letra.isalpha():
            consoantes.append(letra)

    print(f"\nNúmero de vogais: {total}")
    formatadas = ', '.join([f"'{consoante}'" for consoante in consoantes])
    print(f"Consoantes: [{formatadas}]")

def main():
    print("Bem-vindo ao programa de processamento de dados!")
    while True:
        try:
            n = int(input('\nDigite o número de elementos para processar: '))
            if n < 0:
                print("Por favor, insira um número inteiro não negativo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro não negativo.")
    
    reais(n)
    escola(n)
    letras(n)

if __name__ == '__main__':
    main()
