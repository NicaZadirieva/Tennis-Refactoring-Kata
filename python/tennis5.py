from player import Player


class TennisGame5:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def score(self):
        maximum = max(self.player1.points, self.player2.points)
        if maximum > 4:
            self.player1.points -= max(maximum - 4, 0)
            self.player2.points -= max(maximum - 4, 0)

        while self.player1.points > 4 or self.player2.points > 4:
            self.player1.points -= 1
            self.player2.points -= 1

        if self.player1.points < 3 and self.player2.points == 4:
            return "Win for player2"
        elif self.player1.points == 3 and self.player2.points == 4:
            return "Advantage player2"
        elif self.player2.points < 3 and self.player1.points == 4:
            return "Win for player1"
        elif self.player1.points == 4 and self.player2.points == 3:
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
        elif self.player1.points == 3 and self.player2.points != 3:
            player2_score = {0: "Love", 1: "Fifteen", 2: "Thirty"}.get(
                self.player2.points, ""
            )
            return "Forty-" + player2_score
        elif (
            self.player1.points == 3
            and self.player2.points == 3
            or self.player1.points == 4
            and self.player2.points == 4
        ):
            return "Deuce"
