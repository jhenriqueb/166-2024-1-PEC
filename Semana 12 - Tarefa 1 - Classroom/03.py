def main():
    print("Bem-vindo ao simulador de crescimento populacional!")
    print("Por favor, insira a população do primeiro grupo:")
    p1 = int(input("População do Grupo A: "))
    print("Agora, insira a população do segundo grupo:")
    p2 = int(input("População do Grupo B: "))

    if p1 > p2:
        populacao_a = p1
        populacao_b = p2
        grupo_a = "Grupo A"
        grupo_b = "Grupo B"
    elif p2 > p1:
        populacao_a = p2
        populacao_b = p1
        grupo_a = "Grupo B"
        grupo_b = "Grupo A"
    else:
        print("As populações são iguais. Não será possível determinar qual grupo se tornará mais populoso.")
        return

    print(f"Inicialmente, {grupo_a} tem a maior população com {populacao_a} e {grupo_b} tem {populacao_b}.")

    anos = 0
    while True:
        taxa_n_a = ((2 / 100) * populacao_a)
        taxa_n_b = ((3 / 100) * populacao_b)
        populacao_a += round(taxa_n_a)
        populacao_b += round(taxa_n_b)
        anos += 1

        print(f"Ano {anos}: {grupo_a} - {populacao_a} habitantes, {grupo_b} - {populacao_b} habitantes")

        if populacao_b > populacao_a:
            break

    print(f"Depois de {anos} anos, {grupo_b} superou {grupo_a} em população!")

if __name__ == "__main__":
    main()
