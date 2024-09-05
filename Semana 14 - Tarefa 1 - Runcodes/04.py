def coletar_dados(jogadores):
    nomes = []
    alturas = []
    for _ in range(jogadores):
        nome = input()
        altura = float(input())
        nomes.append(nome)
        alturas.append(altura)
    return nomes, alturas

def jogador_mais_alto(nomes, alturas):
    indice_max = alturas.index(max(alturas))
    return nomes[indice_max], alturas[indice_max]

def calcular_media(alturas):
    return sum(alturas) / len(alturas)

def jogadores_acima_da_media(nomes, alturas, media):
    jogadores_acima = []
    for i in range(len(alturas)):
        if alturas[i] > media:
            jogadores_acima.append((nomes[i], alturas[i]))
    return jogadores_acima

num_jogadores = 12

nomes, alturas = coletar_dados(num_jogadores)

nome_mais_alto, altura_mais_alto = jogador_mais_alto(nomes, alturas)
print("JOGADOR MAIS ALTO DO TIME")
print(f"{nome_mais_alto}")
print(f"{altura_mais_alto:.2f}")

media_altura = calcular_media(alturas)
print("ALTURA MÉDIA DO TIME")
print(f"{media_altura:.2f}")

acima_da_media = jogadores_acima_da_media(nomes, alturas, media_altura)
print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
for nome, altura in acima_da_media:
    print(f"{nome}")
    print(f"{altura:.2f}")
