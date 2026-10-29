def backtracking(n, k, i=0, result='', respostas=None):
    if respostas is None:
        respostas = []

    # Condição de parada
    if i == n:
        respostas.append(result)
        if len(respostas) == k:
            return result
        return None

    # Testar as letras a, b, c
    for letra in 'abc':

        # Condição de poda
        if result and result[-1] == letra:
            continue

        resposta = backtracking(n, k, i + 1, result + letra, respostas)

        if resposta is not None:
            return resposta

    return None


def main():
    n, k = map(int, input().split())

    resultado = backtracking(n, k)
    print(resultado if resultado is not None else "vazio")


if __name__ == "__main__":
    main()