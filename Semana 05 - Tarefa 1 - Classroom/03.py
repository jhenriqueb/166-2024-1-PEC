def calcular_aumento(preco, percentual): 
    return preco * (1+ percentual/100)

def calcular_desconto(preco, percentual):
    return preco * (1- percentual/100)

def main():
    preco = float(input('Digite o preço: '))
    percentual = float(input('Digite o percentual: '))
    
    preco_aumento = calcular_aumento(preco, percentual)
    preco_desconto = calcular_desconto(preco, percentual)

    print(f'O preço com aumento: {preco_aumento:.2f}')
    print(f'O preco com desconto: {preco_desconto:.2f}')
    
if __name__ == '__main__':
    main()