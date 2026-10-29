def keyboard(words):
    linha1 = "qwertyuiop"
    linha2 = "asdfghjkl"
    linha3 = "zxcvbnm"
    results = ""

    #linha 1
    for word in words:
        resultLinha1 = True
        for letra in word.lower():
            if letra not in linha1:
                resultLinha1 = False
                break
        if resultLinha1:
            results += word + " "

    #linha 2
    for word in words:
        resultLinha2 = True
        for letra in word.lower():
            if letra not in linha2:
                resultLinha2 = False
                break
        if resultLinha2:
            results += word + " "

    #linha 3
    for word in words:
        resultLinha3 = True 
        for letra in word.lower():
            if letra not in linha3:
                resultLinha3 = False
                break
        if resultLinha3:
            results += word + " "

    return results


def main():
    t = int(input())
    words = list(map(str, input().split()))
    resultado = keyboard(words)
    if resultado == "":
        print("vazio")
    else:
        print(resultado)


if __name__ == "__main__":
    main()