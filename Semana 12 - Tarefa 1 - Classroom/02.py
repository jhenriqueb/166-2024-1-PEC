def calcular_meses_para_comprar(preco_inicial_carro):
    saldo_poupanca = 10000
    rendimento_poupanca = 0.007
    aumento_preco_carro = 0.004
    meses = 0
    
    while saldo_poupanca < preco_inicial_carro:
        saldo_poupanca += saldo_poupanca * rendimento_poupanca
        preco_inicial_carro += preco_inicial_carro * aumento_preco_carro
        meses += 1
    
    return meses

def main():
    preco_inicial_carro = float(input("Digite o preço do carro hoje: "))
    meses = calcular_meses_para_comprar(preco_inicial_carro)
    print(f"Você terá dinheiro suficiente para comprar o carro em {meses} meses.")

if __name__ == "__main__":
    main()
