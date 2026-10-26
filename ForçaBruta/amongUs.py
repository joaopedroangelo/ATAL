# É dado um array A consistindo de N (N ≥ 3) integers positivos. 
# Nesse array, todos os números com a exceção de um são iguais.
# Imprima o index do número diferente. 
# Obs.: a contagem do index no array deve começar do 1!

# ENTRADA: A primeira linha contém apenas um integer positivo T (1 ≤ T ≤ 100), que determina a quantidade de casos de teste.
# ENTRADA: A primeira linha de cada caso de teste contém um único integer N(3 ≤ N ≤ 100), o tamanho do array A.
# ENTRADA: A segunda linha de cada caso de teste contém N integers a1, a2 ,…, an (1 ≤ ai ≤ 100).
# SAÍDA: Para cada caso de teste, imprima um único integer, o index do número diferente.


def amongUs(n, arr):
    indice = -1
    for i in range(0, len(arr)):
        diferente = 0
        igual = 0
        for j in range(0, len(arr)):
            if arr[i] == arr[j] and i != j:
                igual += 1
            if arr[i] != arr[j] and i != j:
                diferente += 1
        if diferente > igual: 
            indice = i
    return indice


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(amongUs(n, arr) + 1)

if __name__ == "__main__":
    main()