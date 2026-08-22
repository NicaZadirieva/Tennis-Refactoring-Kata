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

        if (
            self.player1.points < DEUCE_THRESHOLD
            and self.player2.points == WIN_THRESHOLD
        ):
            return "Win for player2"
        elif (
            self.player1.points == DEUCE_THRESHOLD
            and self.player2.points == WIN_THRESHOLD
        ):
            return "Advantage player2"
        elif (
            self.player2.points < DEUCE_THRESHOLD
            and self.player1.points == WIN_THRESHOLD
        ):
            return "Win for player1"
        elif (
            self.player1.points == WIN_THRESHOLD
            and self.player2.points == DEUCE_THRESHOLD
        ):
            return "Advantage player1"
        elif self.player1.points == 0:
            player2_score = {0: "All", 1: "Fifteen", 2: "Thirty", 3: "Forty"}.get(
                self.player2.points, ""
            )
            return "Love-" + player2_score
        elif self.player1.points == 1:
            player2_score = {0: "Love", 1: "All", 2: "Thirty", 3: "Forty"}.get(
                self.player2.points, ""
            )
            return "Fifteen-" + player2_score
        elif self.player1.points == 2:
            player2_score = {0: "Love", 1: "Fifteen", 2: "All", 3: "Forty"}.get(
                self.player2.points, ""
            )
            return "Thirty-" + player2_score
        elif (
            self.player1.points == DEUCE_THRESHOLD
            and self.player2.points != DEUCE_THRESHOLD
        ):
            player2_score = {0: "Love", 1: "Fifteen", 2: "Thirty"}.get(
                self.player2.points, ""
            )
            return "Forty-" + player2_score
        elif self.player1.points == self.player2.points:
            return "Deuce"
