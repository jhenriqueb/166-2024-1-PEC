preco = float(input('Digite um preço: '))
desconto = preco * 0.10
preco_com_desconto = preco - desconto
preco_final = round(preco_com_desconto, 2)
print(f'O preço com 10% de desconto: {preco_final}R$')