def selfDivisible(limite_inferior, limite_superior):
    result = ""
    for num in range(limite_inferior, limite_superior + 1):
        num_str = str(num)
        for digit in num_str:
            self_dividible = True
            if digit == '0': 
                self_dividible = False
                break
            if num % int(digit) == 0:
                continue
            else:
                self_dividible = False
                break
        if self_dividible:
            result += str(num) + " "
    return result


def main():
    limite_inferior, limite_superior = map(int, input().split())
    resultado = selfDivisible(limite_inferior, limite_superior)
    print(resultado)


if __name__ == "__main__":
    main()
