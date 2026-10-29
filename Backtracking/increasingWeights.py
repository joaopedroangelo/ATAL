def backtracking(n, i=0, result=''):
    if i == 3:
        for comparacao in n:
            a, op, b = comparacao

            if op == '<' and result.index(a) > result.index(b):
                return None

            if op == '>' and result.index(a) < result.index(b):
                return None

        return result

    for moeda in 'ABC':
        if moeda not in result:
            resposta = backtracking(n, i + 1, result + moeda)

            if resposta is not None:
                return resposta

    return None


def main():
    n = [input().strip() for _ in range(3)]
    resultado = backtracking(n)
    print(resultado if resultado is not None else 'Impossible')


if __name__ == "__main__":
    main()