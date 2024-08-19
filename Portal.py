from random import*

jogando = True
score = 0

print('''
Portal da Fortuna!
=================
      

Existe um Super prémio atrás de uma dessas 3 portas!
Adivinhe qual é a porta certa para ganhar o premio!
    _______        _______        _______
   |       |      |       |      |       |
   |  [1]  |      |   [2] |      |   [3] |
   |      °|      |      °|      |      °|
   |_______|      |_______|      |_______|
      
''')

while jogando :
        print("\nEscolha uma porta(1, 2 ou 3):")

        portaEscolhida = int(input())

        aleatorio = randint(1,3)
        print('A porta escolhida foi a' , portaEscolhida)
        print('A porta certa é ', aleatorio)
        if portaEscolhida == aleatorio:
          print("Parabens!!!")
          score += 1
        else:
           print("Que peninha!")

        print("Sua pontuaçao é ", score)

        print("\nVocê quer jogar de novo? (s/n)")
        resposta = input()

        if resposta == 'n':
           jogando = False
           print("Obrigado por jogar!!!")
           print("Sua pontuaçao final é de ", score)
        else:
           jogando == True

    



