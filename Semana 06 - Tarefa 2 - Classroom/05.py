def temperatura(x):
    return((x * (9 / 5)) + 32)

def main():
    celsius = float(input().strip())
    fah = temperatura(celsius)

    print(f'{fah:.2f}')

if __name__ == "__main__":
    main()