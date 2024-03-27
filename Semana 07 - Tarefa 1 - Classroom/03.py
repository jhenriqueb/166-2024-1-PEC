def verificar_sinal(cor):
    if cor == "V":
        return "Siga"
    elif cor == "A":
        return "Atenção"
    elif cor == "E":
        return "Pare"
    else:
        return "Cor inválida"
    
def main():
    
    cor_sinal = input('Digite qual cor de sinal deseja: ').upper().strip()
    mensagem = verificar_sinal(cor_sinal)
    print(mensagem)

if __name__ == '__main__':
    main()