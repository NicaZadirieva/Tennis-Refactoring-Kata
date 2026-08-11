from player import Player


class TennisGame1:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def score(self):
        result = ""
        temp_score = 0
        if self.player1.points == self.player2.points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1.points, "Deuce")
        elif self.player1.points >= 4 or self.player2.points >= 4:
            minus_result = self.player1.points - self.player2.points
            if minus_result == 1:
                result = "Advantage player1"
            elif minus_result == -1:
                result = "Advantage player2"
            elif minus_result >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.points
                else:
                    result += "-"
                    temp_score = self.player2.points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
