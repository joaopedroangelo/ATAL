def backtracking(n, i=0, result=''):
    length = n[0].__len__()
    if (i==length):
        if result not in n:
            return result
        else:
            return None
        
    result1 = backtracking(n, i+1, result+'0')
    if result1 is not None:
        return result1

    result2 = backtracking(n, i+1, result+'1')
    if result2 is not None:
        return result2


def main():
    n = list(map(str, input().split()))
    print(backtracking(n))


if __name__ == "__main__":
    main()