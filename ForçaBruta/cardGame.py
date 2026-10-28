# Cada carta tem um valor inteiro entre 1 e 10;
# Cada jogador recebe duas cartas que estão viradas para baixo;
# Em cada rodada, ambos os jogadores escolhem uma carta para jogar;
# O jogador que escolher a carta de maior valor ganha a rodada;
# Vence o jogo quem ganhar mais rodadas.

# ENTRADA: A primeira linha da entrada é o número de casos de teste t (1 ≤ t ≤ 1000).
# ENTRADA: Cada caso de teste consiste em uma linha com quatro inteiros a1, a2, b1 e b2 (1 ≤ a1, a2, b1, b2 ≤ 10), representando as cartas dos jogadores A e B.
# SAÍDA: Para cada caso de teste, imprima um único inteiro que representa o número de jogos que o jogador A venceria, considerando todos os possíveis.


def card_game(a1, a2, b1, b2):
    num_games_won_a = 0

    for cards_a in ((a1, a2), (a2, a1)):
        for cards_b in ((b1, b2), (b2, b1)):
            wins_a = 0
            wins_b = 0

            if cards_a[0] > cards_b[0]:
                wins_a += 1
            elif cards_a[0] < cards_b[0]:
                wins_b += 1

            if cards_a[1] > cards_b[1]:
                wins_a += 1
            elif cards_a[1] < cards_b[1]:
                wins_b += 1

            if wins_a > wins_b:
                num_games_won_a += 1

    return num_games_won_a


def main():
    t = int(input())
    for number_inputs in range(t):
        a1, a2, b1, b2 = map(int, input().split())
        print(card_game(a1, a2, b1, b2))


if __name__ == "__main__":
    main()