def calcular_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

def main():
    tempo_em_segundos = int(input('Digite quantos segundos: '))

    horas, minutos, segundos = calcular_tempo(tempo_em_segundos)

    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

if __name__ == "__main__":
    main()