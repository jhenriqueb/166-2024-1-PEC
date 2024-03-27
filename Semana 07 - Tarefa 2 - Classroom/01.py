def estado(x, n):
    if x == 1:
        conjuge = input().strip()
        return(len(n) + len(conjuge))
    else:
        return(len(n))
    
def main():
    nome = input('Digite o seu nome: ')
    status = int(input('Digite seu estado civil(Casado[1] Solteiro[2]): '))

    res = estado(status, nome)

    print(f'A soma das letras se você é solteiro ou casado é: {res}')

if __name__ == '__main__':
    main()