import string
import random

def criar_alfabeto_embaralhado():
    alfabeto = list(string.ascii_lowercase)
    random.shuffle(alfabeto)
    return ''.join(alfabeto)

def criar_alfabeto_embaralhado_maiusculas():
    alfabeto = list(string.ascii_uppercase)
    random.shuffle(alfabeto)
    return ''.join(alfabeto)

def criptografar(texto, chave):
    alfabeto = criar_alfabeto_embaralhado()
    alfabeto_maiusculas = criar_alfabeto_embaralhado_maiusculas()
    
    resultado = ""
    chave_atual = chave
    
    for char in texto:
        if char.isalpha():
            if char.islower():
                index = alfabeto.index(char)
                novo_char = alfabeto[(index + chave_atual) % 26]
            elif char.isupper():
                index = alfabeto_maiusculas.index(char)
                novo_char = alfabeto_maiusculas[(index + chave_atual) % 26]
            resultado += novo_char
            chave_atual += 1  # Incrementa a chave após criptografar cada letra
        else:
            # Remove caracteres não alfabéticos
            continue

    return resultado

def descriptografar(texto, chave):
    alfabeto = criar_alfabeto_embaralhado()
    alfabeto_maiusculas = criar_alfabeto_embaralhado_maiusculas()
    
    resultado = ""
    chave_atual = chave
    
    for char in texto:
        if char.isalpha():
            if char.islower():
                index = alfabeto.index(char)
                novo_char = alfabeto[(index - chave_atual) % 26]
            elif char.isupper():
                index = alfabeto_maiusculas.index(char)
                novo_char = alfabeto_maiusculas[(index - chave_atual) % 26]
            resultado += novo_char
            chave_atual += 1  # Incrementa a chave após descriptografar cada letra
        else:
            # Remove caracteres não alfabéticos
            continue

    return resultado

def main():
    texto = input("Digite o texto para criptografar: ")
    
    while True:
        try:
            chave = int(input("Digite a chave de criptografia (um número inteiro): "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro para a chave.")
    
    texto_criptografado = criptografar(texto, chave)
    texto_criptografado_sem_espacos = ''.join(texto_criptografado.split())
    print(f"Texto criptografado (sem espaços e caracteres especiais): {texto_criptografado_sem_espacos}")
    
    mensagem_criptografada = input("Digite a mensagem criptografada para descriptografar: ")
    
    mensagem_descriptografada = descriptografar(mensagem_criptografada, chave)
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")

if __name__ == '__main__':
    main()
