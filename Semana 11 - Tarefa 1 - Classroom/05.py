def conta(x, y):

    mes = 10
    ano = 2016

    while y <= x:
        mes += 1

        if mes > 12:
            mes = 1
            ano += 1
        
        if mes == 3:
            x *= 1.05

        y *= 1.15

    return mes, ano

def main():
    print("Bem-vindo ao calculador de dívida e salário!")
    print("Este programa calcula em que mês e ano a dívida se tornará menor que o salário,")
    print("considerando um aumento de 5% na dívida a cada março e um aumento de 15% no salário a cada mês.")
    
    try:
        salario = float(input("Digite o valor inicial do salário: R$ "))
        divida = float(input("Digite o valor inicial da dívida: R$ "))

        mes, ano = conta(salario, divida)

        print(f'A dívida será menor que o salário em {mes}/{ano}.')
    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos válidos.")

if __name__ == '__main__':
    main()
