from player import Player

WIN_THRESHOLD = 4
DEUCE_THRESHOLD = 3


class TennisGame5:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def __normalize_points__(self):
        maximum_points = max(self.player1.points, self.player2.points)
        if maximum_points > WIN_THRESHOLD:
            self.player1.points -= max(maximum_points - WIN_THRESHOLD, 0)
            self.player2.points -= max(maximum_points - WIN_THRESHOLD, 0)

    def score(self):
        self.__normalize_points__()

        p1 = self.player1.points
        p2 = self.player2.points

        # Победа игрока 2
        if p1 < DEUCE_THRESHOLD and p2 == WIN_THRESHOLD:
            return "Win for player2"

        # Преимущество игрока 2
        if p1 == DEUCE_THRESHOLD and p2 == WIN_THRESHOLD:
            return "Advantage player2"

        # Победа игрока 1
        if p2 < DEUCE_THRESHOLD and p1 == WIN_THRESHOLD:
            return "Win for player1"

        # Преимущество игрока 1
        if p1 == WIN_THRESHOLD and p2 == DEUCE_THRESHOLD:
            return "Advantage player1"

        # Счёт для p1 = 0
        if p1 == 0:
            score_map = {0: "All", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
            return "Love-" + score_map.get(p2, "")

        # Счёт для p1 = 1
        if p1 == 1:
            score_map = {0: "Love", 1: "All", 2: "Thirty", 3: "Forty"}
            return "Fifteen-" + score_map.get(p2, "")

        # Счёт для p1 = 2
        if p1 == 2:
            score_map = {0: "Love", 1: "Fifteen", 2: "All", 3: "Forty"}
            return "Thirty-" + score_map.get(p2, "")

        # Счёт для p1 = 3 (Forty) когда p2 не 3
        if p1 == DEUCE_THRESHOLD and p2 != DEUCE_THRESHOLD:
            score_map = {0: "Love", 1: "Fifteen", 2: "Thirty"}
            return "Forty-" + score_map.get(p2, "")

        # Deuce
        if p1 == p2:
            return "Deuce"
