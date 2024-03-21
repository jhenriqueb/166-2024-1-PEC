def calcular_total_compra(preco_maca, preco_banana):
    return (preco_maca * 3) + (preco_banana * 2)

def main():
    preco_maca = float(input().strip())
    preco_banana = float(input().strip())

    total_compra = calcular_total_compra(preco_maca, preco_banana)

    print(f'{total_compra:.2f}')

if __name__ == "__main__":
    main()