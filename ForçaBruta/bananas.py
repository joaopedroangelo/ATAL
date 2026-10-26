# Kmes escreveu três inteiros a, b e c para se lembrar de que precisa dar a × b × c bananas para Noobish_Monk.
# Noobish_Monk encontrou esses números e decidiu fazer o seguinte no máximo 5 vezes:
# escolher um desses inteiros;
# aumentá-lo em 1.

# Por exemplo, se a = 2, b = 3 e c = 4, é possível aumentar a três vezes em 1 e aumentar b duas vezes em 1. 
# Após isso, a = 5, b = 5 e c = 4. Assim, o número total de bananas será5×5×4=100.
# Qual é o valor máximo de a × b × c que Noobish_Monk pode obter com essas operações?

# ENTRADA: A primeira linha contém um inteiro t ( 1 ≤ t ≤ 1000) — o número de casos de teste.
# ENTRADA: Cada caso de teste consiste em uma única linha contendo três inteiros a, b e c (1≤a,b,c≤10).

# SAÍDA: Para cada caso de teste, imprima um único inteiro — a quantidade máxima de bananas que Noobish_Monk pode obter.


def max_bananas(a, b, c):
    max_product = 0
    for i in range(6):
        for j in range(6 - i):
            aumentos_c = 5 - i - j
            product = (a + i) * (b + j) * (c + aumentos_c)
            if product > max_product:
                max_product = product
    return max_product


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(max_bananas(a, b, c))


if __name__ == "__main__":
    main()
