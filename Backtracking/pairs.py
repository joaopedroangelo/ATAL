def backtrack(w, parte1):
    parte2 = w - parte1
    # Condição de parada: encontramos uma divisão válida
    if (parte1 > 0 and parte2 > 0) and (parte1 % 2 == 0 and parte2 % 2 == 0):
        return "YES"
    # Condição de parada: esgotamos as possibilidades
    if parte1 >= w:
        return "NO"
    # Tenta a próxima possibilidade
    return backtrack(w, parte1 + 1)


def main():
    w = int(input())
    print(backtrack(w, 1))


if __name__ == "__main__":
    main()