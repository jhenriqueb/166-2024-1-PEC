x = 5
y = 3
z = 8
q = int(input('Digite quantos Pó de Lua Estelar você deseja (5 moedas de ouro): '))
w = int(input('Digite quantos Essência de Dragão você deseja (3 moedas de ouro): '))
e = int(input('Digite quantos Lágrimas de Fênix você deseja (8 moedas de ouro): '))
v = ((x*q)+(y*w)+(e*z))
print(f'''
Foram:  {x*q} Pó de Lua Estelar
        {y*w} Essência de Dragão
        {z*e} Lágrimas de Fênix
Total:  {v}
''')