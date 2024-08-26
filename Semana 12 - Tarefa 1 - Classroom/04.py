def calcular_numero_da_sorte(data_nascimento):
    return sum(int(digito) for digito in str(data_nascimento))

def main():
    data_nascimento = int(input("Digite sua data de nascimento no formato ddmmaaaa (8 dígitos): "))
    numero_da_sorte = calcular_numero_da_sorte(data_nascimento)
    print(f"O seu número da sorte é {numero_da_sorte}.")

if __name__ == "__main__":
    main()
