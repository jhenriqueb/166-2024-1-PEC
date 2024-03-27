def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if nota3 > 8:
        media += 1
    if media > 10:
        media = 10
    return media

def main():
    nota1 = float(input('Digite a 1° nota:  '))
    nota2 = float(input('Digite a 2° nota:  '))
    nota3 = float(input('Digite a 3° nota:  '))

    media_final = calcular_media(nota1, nota2, nota3)

    print(f' A media final do aluno é: {media_final}')

if __name__ == '__main__':
    main()