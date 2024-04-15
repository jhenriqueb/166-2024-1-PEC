def calcular(a,b,c):
    if c == 1:
        return (a+b)
    if c == 2:
        return (a-b)
    if c == 3:
        return (a*b)
    if c == 4:
        return(a/b)

def main():
#Entrada
    n1 = float(input('Digite um numero:'))
    n2 = float(input('Digite outro numero:'))
    operacao = int(input('Digite 1 para a adição dos numeros, 2 para subtração, 3 para multiplicação e 4 caso queira a divisão dos numeros.'))

#Processo
    resultado = calcular(n1,n2,operacao)

#Saída
    print('O valor da operação dos dois numeros é',resultado) 

if __name__ == '__main__':
    main()