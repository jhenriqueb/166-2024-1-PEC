def espaco(x):
    return(x//2)

def main():
    idade_t = int(input().strip())
    idade_e = espaco(idade_t)

    print(idade_e)

if __name__ == "__main__":
    main()