def backtracking(itens, W, i=0, peso=0, valor=0):
    # Condição de poda
    if peso > W:
        return -1

    # Condição de parada
    if i == len(itens):
        return valor

    peso_item, valor_item = itens[i]

    # Escolher levar o item
    result1 = backtracking(
        itens, W, i + 1,
        peso + peso_item,
        valor + valor_item
    )

    # Escolher não levar o item
    result2 = backtracking(
        itens, W, i + 1,
        peso,
        valor
    )

    return max(result1, result2)


def main():
    N, W = map(int, input().split())

    itens = []
    for _ in range(N):
        peso, valor = map(int, input().split())
        itens.append((peso, valor))

    print(backtracking(itens, W))


if __name__ == "__main__":
    main()