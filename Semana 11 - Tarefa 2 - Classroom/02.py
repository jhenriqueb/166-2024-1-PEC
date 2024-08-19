def operacoes():

    pessoas = 0
    soma = 0 
    menor = None
    maior = None
   
    print("Bem-vindo ao programa de análise de idades!")
    print("Digite as idades das pessoas. Digite 0 para encerrar a entrada e calcular os resultados.")

    while True:
        try:
            idade = int(input("Digite a idade de uma pessoa: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if idade == 0:
            break

        pessoas += 1
        soma += idade

        if menor is None or idade < menor:
            menor = idade

        if maior is None or idade > maior:
            maior = idade

    if pessoas > 0:
        media = soma / pessoas

        print(f'Número total de pessoas: {pessoas}')
        print(f'Média das idades: {media:.2f}')
        print(f'Menor idade: {menor}')
        print(f'Maior idade: {maior}')
    else:
        print("Nenhuma idade válida foi digitada.")

def main():
    operacoes()

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()