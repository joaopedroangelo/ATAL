def distinctDigits(n):
    while (True):
        n += 1
        n_str = str(n)
        distincts = True
        caracteres_vistos = set()
        for caractere in n_str:
            if caractere in caracteres_vistos:
                distincts = False
                break
            caracteres_vistos.add(caractere)
        if distincts:
            return n


def main():
    n = int(input())
    print(distinctDigits(n))


if __name__ == "__main__":
    main()