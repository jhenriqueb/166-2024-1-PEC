def resposta(a,b,c,d,e):
   positivas = [a,b,c,d,e]
   num = positivas.count("S")

   if num == 5: 
      return ("Assassino")
   elif num in [3,4]:
      return ("Cúmplice")
   elif num == 2:
      return ("Suspeito")
   else:
      return("Inocente")


def main():
#Entrada
   r1 = input( "Telefonou para a vítima ?").upper().strip()
   r2 = input("Esteve no local do crime ?").upper().strip()
   r3 = input("Mora perto da vítima ?").upper().strip()
   r4 = input( "Devia para a vítima ?").upper().strip()
   r5 = input("Já trabalhou com a vítima ?").upper().strip()

#Processo
   veredito = resposta(r1,r2,r3,r4,r5)

#Saída
   print(veredito)

if __name__ == '__main__':
   main()
   