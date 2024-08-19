def resposta():

    print("\nOPÇÕES: ")
    print("1 - SAUDAÇÃO")
    print("2 - BRONCA")
    print("3 - FELICITAÇÃO")
    print("0 - FIM")

def main():
 
    print("Bem-vindo ao sistema de respostas!")
    print("Escolha uma das opções abaixo para receber uma resposta correspondente.")
    
    opcao = -1

    while opcao != 0:
        resposta()

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if opcao == 1:
            print("1 - Olá. Como vai?")

        elif opcao == 2:
            print("2 - Vamos estudar mais.")

        elif opcao == 3:
            print("3 - Meus Parabéns!")
        
        elif opcao == 0:
            print("0 - Fim de serviço.")
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()


