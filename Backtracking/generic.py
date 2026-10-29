def backtrack(X, i, resultados):
    # Verifica se a solucao esta completa
    if i == len(X):
        resultados.append(X.copy())
        return
    # Testa os candidatos para a posicao atual
    for x in candidatos(X, i):
        if consistente(X, i, x):
            X[i] = x
            backtrack(X, i + 1, resultados)
            X[i] = None


def candidatos(X, i):
    # Exemplo: valores possiveis de 1 a 3
    return [1, 2, 3]


def consistente(X, i, x):
    # Exemplo: nao permite repetir valores
    return x not in X[:i]
