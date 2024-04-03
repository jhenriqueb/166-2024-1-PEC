def calcular_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento):
    idade = ano_atual - ano_nascimento
    if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
        idade -= 1
    return idade

def main():
    dia_atual = int(input('Digite o dia atual: '))
    mes_atual = int(input('Digite o mês atual: '))
    ano_atual = int(input('Digite o ano atual: '))

    
    dia_nascimento = int(input('Digite o ano de nascimento: '))
    mes_nascimento = int(input('Digite o mês de nascimento: '))
    ano_nascimento = int(input('Digite o ano de nascimento: '))

    idade = calcular_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento)

    print(f'Sua idade é: {idade}')

if __name__ == "__main__":
    main()
