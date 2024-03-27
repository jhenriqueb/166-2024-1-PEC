def obter_signo(dia, mes):


    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        return "Gêmeos"
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    else:
        return "Peixes"

def main():
    dia = int(input('Digite o dia do seu aniversário: '))
    mes = int(input('Digite o mês do seu anivarsário: '))

    signo = obter_signo(dia, mes)
    print(signo)

if __name__ == "__main__":
    main()
