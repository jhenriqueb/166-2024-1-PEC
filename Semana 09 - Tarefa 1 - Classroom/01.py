def mensagem(x,y,z):
    if x == y and x == z:
        return('Todos os valores são iguais')
    if x != y and x != z and y != z:
        return('Todos os valores são diferentes')
    else: 
        return('Existem dois valores iguais e um diferente')

def main():
#Entrada
    n1 = int(input('Digite o primeiro numero:'))
    n2 = int(input('Digite o segundo numero:'))
    n3 = int(input('Digite o terceiro numero:'))

#Processo
    resultado = mensagem(n1,n2,n3)

#Saída
    print(resultado)


if __name__ == '__main__':
    main()