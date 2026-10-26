# Um inteiro é chamado de inteiro da sorte quando sua frequência no vetor é igual ao seu próprio valor.
# Dado um vetor de inteiros arr, encontre o maior inteiro da sorte presente no vetor.
# Se não existir nenhum inteiro da sorte, imprima -1.
# ENTRADA: A primeira linha contém um inteiro n, representando o tamanho do vetor.
# ENTRADA: A segunda linha contém n inteiros.
# SAÍDA: Imprima o maior inteiro da sorte do vetor. Se não existir, imprima -1.

def largest_lucky(size, numbers):
    frequencies = {}
    
    for number in numbers:
        if number in frequencies:
            frequencies[number] += 1
        else:
            frequencies[number] = 1

    largest_lucky_number = -1
    for number, frequency in frequencies.items():
        if number == frequency and number > largest_lucky_number:
            largest_lucky_number = number
    
    return largest_lucky_number


entrada01 = [4, [2, 2, 3, 4]]
entrada02 = [6, [1, 2, 2, 3, 3, 3]]
entrada03 = [5, [2, 2, 2, 3, 3]]
assert largest_lucky(*entrada01) == 2
assert largest_lucky(*entrada02) == 3
assert largest_lucky(*entrada03) == -1