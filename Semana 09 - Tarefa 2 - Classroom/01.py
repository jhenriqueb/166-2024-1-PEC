def semana(x):
    if x == 1:
        return('domingo')
    elif x == 2:
        return('segunda-feira')
    elif x == 3:
        return('terça-feira')
    elif x == 4:
        return('quarta-feira')
    elif x == 5:
        return('quinta-feira')
    elif x == 6:
        return('sexta-feira')
    elif x == 7:
        return('sábado')
    else:
        return('valor inválido')


def main():
#Entrada
    d = int(input('Digite um numero de 1 a 7, correspondente aos dias da semana:'))

#Processo
    resultado = semana(d)

#Saída
    print(resultado)
    
    
if __name__ == '__main__':
    main()