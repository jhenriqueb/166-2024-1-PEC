def valida(x):
    ano = x%10000
    x = x//10000
    mes = x%100
    x = x//100
    dia = x

#Se o ano for bissexto(fev. 29)
    if (ano%4 == 0) and (ano%100 != 0) or (ano%400 == 0):
        if (1000 <= ano <= 9999) and (1 <= mes <= 12):
            if mes == 2:
                return True if (0 < dia <= 29) else False
            else:
                if mes in [1,3,5,7,8,10,12]:
                    return True if (0 < dia <= 31) else False
                if mes in [4,6,9,11]:
                    return True if (0 < dia <= 30) else False
        else:
            return False
#Se Não for bissexto(fev. 28)        
    else:
         if (1000 <= ano <= 9999) and (1 <= mes <= 12):
             if mes == 2:
                 return True if (0 < dia <= 28) else False
             else:
                 if mes in [1,3,5,7,8,10,12]:
                    return True if (0 < dia <= 31) else False
                 if mes in [4,6,9,11]:
                    return True if (0 < dia <= 30) else False
         else:
             return False

                 
def main():
#Entrada
    data = int(input("Digite uma data:"))

#Processo
    resultado = valida(data)

#Saída
    print(resultado)


if __name__ == '__main__':
    main()