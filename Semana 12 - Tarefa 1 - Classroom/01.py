# Função para calcular o tempo necessário para a lebre alcançar a tartaruga
def calcular_tempo_para_alcancar(distancia_inicial):
    velocidade_tartaruga = 1  # metros por minuto
    velocidade_lebre = 10  # metros por minuto
    
    # A diferença de velocidade entre a lebre e a tartaruga
    diferenca_velocidade = velocidade_lebre - velocidade_tartaruga
    
    # Calcular o tempo necessário para a lebre alcançar a tartaruga
    tempo_necessario = distancia_inicial / diferenca_velocidade
    
    return tempo_necessario

# Função principal
def main():
    # Solicitar ao usuário a distância inicial
    distancia_inicial = float(input("Digite a distância inicial (em metros) que a tartaruga está à frente da lebre: "))
    
    # Calcular o tempo necessário para a lebre alcançar a tartaruga
    tempo_necessario = calcular_tempo_para_alcancar(distancia_inicial)
    
    # Exibir o resultado
    print(f"A lebre alcançará a tartaruga em {tempo_necessario:.2f} minutos.")

# Executar a função principal
if __name__ == "__main__":
    main()
