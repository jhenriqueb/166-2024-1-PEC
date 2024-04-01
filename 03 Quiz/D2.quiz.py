score = 0 

print('''
Q1 - Quais o menor e o maior país do mundo?
a - Vaticano e Rússia
b - Nauru e China
c - Mônaco e Canadá
''')
resposta = input().lower()

if resposta == "a":
    print(" Correto !!!")
    score += 1
elif resposta == "b":
    print(" Não foi hoje !!!")
elif resposta == "c":
    print(" Boa sorte na proxima !!!")
else:
    print("Você não escolheu uma das alternativas!")



print('''
Q2 - O que a palavra legend significa em português?
a - Legenda
b - Conto
c - Lenda
''')
segunda = input().lower()

if segunda == "a":
    print(" Boa sorte na proxima !!!")
elif segunda == "b":
    print(" Não foi hoje !!!")
elif segunda == "c":
    print(" Correto !!!")
    score += 1
else:
    print("Você não escolheu uma das alternativas!")

print('''
Q3 - Quanto tempo a luz do Sol demora para chegar à Terra?
a - 12 minutos
b - 1 dia
c - 8 minutos
''')
terceira = input().lower()

if terceira == "a":
    print(" Boa sorte na proxima !!!")
elif terceira == "b":
    print(" Não foi hoje !!!")
elif terceira == "c":
    print(" Correto !!!")
    score += 1
else:
    print("Você não escolheu uma das alternativas!")

print(f'Você fez {score} pontos!')

if score == 3:
    print(" Very Good !!!")
else:
    print(" Tente novamente")

