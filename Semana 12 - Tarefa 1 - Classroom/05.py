def main():
    print("Bem-vindo ao simulador de crescimento e declínio populacional!")
    print("Por favor, insira a população inicial:")
    populacao_original = int(input("População inicial: ").strip())

    populacao = populacao_original
    ano = 1599

    print(f"\nSimulando a população a partir do ano {ano}...\n")
    print(f"{'Ano':<6} {'Nascimentos':<12} {'Mortes':<6} {'População':<12}")
    print("-" * 40)

    while True:
        num_nascimento = (1 / 100) * populacao
        num_mortes = (6 / 100) * populacao
        total_ano = (num_nascimento + populacao) - num_mortes
        ano += 1
        populacao = total_ano

        print(f"{ano:<6} {round(num_nascimento):<12} {round(num_mortes):<6} {round(total_ano):<12}")

        if total_ano < ((10 / 100) * populacao_original):
            break

    print(f"\nA população caiu abaixo de 10% da população original no ano {ano}.")

if __name__ == "__main__":
    main()
