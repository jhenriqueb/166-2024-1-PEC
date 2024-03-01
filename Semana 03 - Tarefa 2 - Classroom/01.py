pi = 3.141592
raio = float(input('Digite o número do raio: '))
circu = 2 * pi * raio 
a_circu = pi * raio **2
a_esfera = 4 * pi * raio ** 2 
vol_esfera = 4/3 * pi * raio ** 3 

print(f"Circunferência: {circu:.6f}")
print(f"Área do circulo: {a_circu:.6f}")
print(f"Área da esfera: {a_esfera:.6f}")
print(f"Volume da esfera: {vol_esfera:.6f}")