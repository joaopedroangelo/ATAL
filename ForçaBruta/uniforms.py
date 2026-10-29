def uniforms(uniforms_lists):
    cont = 0
    for casa1, visitante1 in uniforms_lists:
        for casa2, visitante2 in uniforms_lists:
            if casa1 == visitante2:
                cont += 1
    return cont


def main():
    n = int(input())
    lista = []
    for _ in range(n):
        casa, visitante = map(int, input().split())
        lista.append((casa, visitante))
    print(uniforms(lista))


if __name__ == "__main__":
    main()