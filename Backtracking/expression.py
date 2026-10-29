def backtracking(a, b, c, i=0, ops=[]):
    if (i==2):
        op1, op2 = ops

        # calcula (a op1 b) op c
        if op1 == '+':
            partial = a + b
        else:
            partial = a * b
        if op2 == '+':
            result1 = partial + c
        else:
            result1 = partial * c

        # calcula a op1 (b op2 c)
        if op2 == '+':
            partial = b + c
        else:
            partial = b * c
        if op2 == '+':
            result2 = a + partial
        else:
            result2 = a * partial

        return max(result1, result2)


    ops.append('+')
    result1 = backtracking(a, b, c, i+1, ops)
    ops.pop()

    ops.append('*')
    result2 = backtracking(a, b, c, i+1, ops)
    ops.pop()
    
    return max(result1, result2)


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(backtracking(a, b, c))


if __name__ == "__main__":
    main()
    
    