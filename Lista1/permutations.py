def backtracking(nums, i=0, result=[]):
    # Condição de parada
    if i == len(nums):
        return 1

    total = 0

    # Escolher um número
    for numero in nums:
        if numero not in result:
            result.append(numero)

            total += backtracking(nums, i + 1, result)

            # Desfazer a escolha
            result.pop()

    return total


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    print(backtracking(nums))


if __name__ == "__main__":
    main()