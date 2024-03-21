def arredondar_para_inteiro(dinheiro):
    dinheiro_arredondado = round(dinheiro)
    return dinheiro_arredondado

def main():
    dinheiro = float(input("Digite uma quantidade de dinheiro: "))
    dinheiro_arredondado = arredondar_para_inteiro(dinheiro)
    print("Valor arredondado:", dinheiro_arredondado)

if __name__ == "__main__":
    main()