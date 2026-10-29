def brute_force(n):
    for i in range(1, n + 1):
        if all(digito in '47' for digito in str(i)):
            if n % i == 0:
                return "YES"

    return "NO"


def main():
    n = int(input())
    print(brute_force(n))


if __name__ == "__main__":
    main()