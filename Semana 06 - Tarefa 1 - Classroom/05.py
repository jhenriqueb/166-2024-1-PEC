def calcular_pagamento(valor_compra):
    valor_vista = valor_compra * 0.91
    valor_prestacao_5x = valor_compra / 5
    valor_prestacao_10x = valor_compra * 1.17 / 10
    return valor_vista, valor_prestacao_5x, valor_prestacao_10x

def main():
    valor_compra = float(input('Digite o valor da comprar: '))
    valor_vista, valor_prestacao_5x, valor_prestacao_10x = calcular_pagamento(valor_compra)
    print(f"Valor para pagamento à vista: R$ {valor_vista:.2f}")
    print(f"Valor da prestação para pagamento em 5 vezes: R$ {valor_prestacao_5x:.2f}")
    print(f"Valor da prestação para pagamento em 10 vezes: R$ {valor_prestacao_10x:.2f}")

if __name__ == "__main__":
    main()