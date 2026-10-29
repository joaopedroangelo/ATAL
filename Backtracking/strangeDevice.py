def strangeDevice(actual, objective, count=0, visited=set(), limit=None):
    if limit is None:
        limit = 2 * max(actual, objective)

    if actual == objective:
        return count

    if actual <= 0 or actual >= limit:
        return float('inf')

    if actual in visited:
        return float('inf')

    visited.add(actual)

    vermelho = strangeDevice(actual * 2, objective, count + 1, visited, limit)
    azul = strangeDevice(actual - 1, objective, count + 1, visited, limit)

    visited.remove(actual)

    return min(vermelho, azul)


def main():
    actual, objective = map(int, input().split())
    print(strangeDevice(actual, objective))


if __name__ == "__main__":
    main()