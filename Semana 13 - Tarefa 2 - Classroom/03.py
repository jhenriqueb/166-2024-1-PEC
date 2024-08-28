def main():
    notas = []
    indices_aprovados = []
    
    print("Digite as notas de 50 alunos:")
    
    for i in range(50):
        while True:
            try:
                nota = float(input(f"Nota do aluno {i + 1}: "))
                if 0 <= nota <= 10:  
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    for i, nota in enumerate(notas):
        if nota >= 6:
            indices_aprovados.append(i)

    print("Índices dos alunos com nota maior ou igual a 6:")
    print(indices_aprovados)

if __name__ == "__main__":
    main()
