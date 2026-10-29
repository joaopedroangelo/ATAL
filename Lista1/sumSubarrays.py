def brute_force(arr):
    total = 0
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            subarray = arr[i:j+1]

            if len(subarray) % 2 != 0:
                total += sum(subarray)

    return total


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    print(brute_force(arr))


if __name__ == "__main__":
    main()