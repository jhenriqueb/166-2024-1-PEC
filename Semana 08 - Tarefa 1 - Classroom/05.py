def calcular_imc(massa, altura):
    return massa / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obeso leve"
    elif imc < 40:
        return "Obeso moderado"
    else:
        return "Obeso mórbido"

def main():
    massa = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))

    imc = calcular_imc(massa, altura)
    classificacao = classificar_imc(imc)

    print(f'A média do IMC é: {imc:.2f}')
    print(classificacao)

if __name__ == "__main__":
    main()
