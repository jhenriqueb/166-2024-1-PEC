def verificar_data_recente(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return dia1, mes1, ano1
    elif ano1 < ano2:
        return dia2, mes2, ano2
    else:
        if mes1 > mes2:
            return dia1, mes1, ano1
        elif mes1 < mes2:
            return dia2, mes2, ano2
        else:
            if dia1 > dia2:
                return dia1, mes1, ano1
            elif dia1 < dia2:
                return dia2, mes2, ano2
            else:
                return dia1, mes1, ano1 

def main():
    dia1 = int(input('Dia 1: '))
    mes1 = int(input('Mês 1: '))
    ano1 = int(input('Ano 1: '))

    dia2 = int(input('Dia 2: '))
    mes2 = int(input('Mês 2: '))
    ano2 = int(input('Ano 2: '))

    dia_recente, mes_recente, ano_recente = verificar_data_recente(dia1, mes1, ano1, dia2, mes2, ano2)

    print(f'Data mais recente: {dia_recente}/{mes_recente}/{ano_recente}')

if __name__ == "__main__":
    main()
