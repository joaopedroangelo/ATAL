# Um número mágico é um número formado pela concatenação dos números 1 , 14 e 144.
# Podemos usar cada um desses números qualquer quantidade de vezes.
# Portanto, 14144 , 141414 e 1411 são números mágicos, mas 1444 , 514 e 414 não são.
# Exercício: Você vai receber um número. Determine se ele é um número mágico ou não.
# Entrada: A primeira linha da entrada contém um número inteiro n , (1 ≤  n  ≤ 10 ) . Este número não contém zeros à esquerda. 
# Saída: Imprima " SIM " se n for um número mágico ou imprima " NÃO " se não for. 


def is_magic_number(n):
    n_str = str(n)
    i = 0
    while i < len(n_str):
        if n_str[i:i+3] == '144':
            i += 3
        elif n_str[i:i+2] == '14':
            i += 2
        elif n_str[i:i+1] == '1':
            i += 1
        else:
            return "NÃO"
    return "SIM"


n_teste1 = 114114
n_teste2 = 1111
n_teste3 = 441231 
n_teste4 = 55

assert is_magic_number(n_teste1) == "SIM"
assert is_magic_number(n_teste2) == "SIM"
assert is_magic_number(n_teste3) == "NÃO"
assert is_magic_number(n_teste4) == "NÃO"