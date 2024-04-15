def quantidade(x):
    if 0 < x < 1000:
        u = x%10
        x //= 10
        d = x%10
        x //= 10
        c = x%10
        return c,d,u
    
def centenas(c):
    if c == 1:
        qntd = 'uma centena'
    elif c == 2:
        qntd = 'duas centenas'
    elif c == 3:
        qntd = 'três centenas'
    elif c == 4:
        qntd = 'quatro centenas'
    elif c == 5:
        qntd = 'cinco centenas'
    elif c == 6:
        qntd = 'seis centenas'
    elif c == 7:
        qntd = 'sete centenas'
    elif c == 8:
        qntd = 'oito centenas'
    elif c == 9:
        qntd = 'nove centenas'
    return qntd

def dezenas(d):
    if d == 1:
        qntd = 'uma dezena'
    elif d == 2:
        qntd = 'duas dezenas'
    elif d == 3:
        qntd = 'três dezenas'
    elif d == 4:
        qntd = 'quatro dezenas'
    elif d == 5:
        qntd = 'cinco dezenas'
    elif d == 6:
        qntd = 'seis dezenas'
    elif d == 7:
        qntd = 'sete dezenas'
    elif d == 8:
        qntd = 'oito dezenas'
    elif d == 9:
        qntd = 'nove dezenas'
    return qntd

def unidade(u):
    if u == 1:
        qntd = 'uma unidade'
    elif u == 2:
        qntd = 'duas unidades'
    elif u == 3:
        qntd = 'três unidades'
    elif u == 4:
        qntd = 'quatro unidades'
    elif u == 5:
        qntd = 'cinco unidades'
    elif u == 6:
        qntd = 'seis unidades'
    elif u == 7:
        qntd = 'sete unidades'
    elif u == 8:
        qntd = 'oito unidades'
    elif u == 9:
        qntd = 'nove unidades'
    return qntd


def main():
#Entrada
    num = int(input('Digite um valor menor que 1000:'))

#Processo
    cent, dez, uni = quantidade(num)

#Saída
    if cent > 0 and dez > 0 and uni > 0:
        print(f'{centenas(cent)}, {dezenas(dez)} e {unidade(uni)}.')
    elif cent == 0 and dez == 0 and uni > 0:
        print(f'{unidade(uni)}.')
    elif cent == 0 and dez > 0 and uni == 0:
        print(f'{dezenas(dez)}.')
    elif cent > 0 and dez == 0 and uni == 0:
        print(f'{centenas(cent)}.')
    elif cent == 0 and dez > 0 and uni > 0:
        print(f'{dezenas(dez)} e {unidade(uni)}.')
    elif cent > 0 and dez > 0 and uni == 0:
        print(f'{centenas(cent)} e {dezenas(dez)}.')
    elif cent > 0 and dez == 0  and uni > 0:
        print(f'{centenas(cent)} e {unidade(uni)}.')


if __name__ == '__main__':
    main()


      
    