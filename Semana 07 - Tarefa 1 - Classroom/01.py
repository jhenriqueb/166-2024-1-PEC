def chamada(no, se):
    if se == 1:
        return(f'Ilmo Sr. {no}')
    else:
        return(f'Ilma Sra. {no}')

def main():
    nome = input('Digite seu nome:')
    sexo = int(input('Digite seu sexo(Masculino[1] Feminino[2]):'))

    res = chamada(nome,sexo)

    print(res)

if __name__ == '__main__':
    main()