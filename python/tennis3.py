from player import Player


class TennisGame3:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def __generate_won_player_name__(self):
        return (
            self.player1.name
            if self.player1.points > self.player2.points
            else self.player2.name
        )

    def __is_advantage_gamer__(self):
        return (
            (self.player1.points - self.player2.points)
            * (self.player1.points - self.player2.points)
        ) == 1

    def score(self):
        if (
            self.player1.points == self.player2.points
            and self.player1.points != 3
            and self.player1.points < 4
        ):
            return {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
                3: "Forty-All",
            }.get(self.player1.points)
        elif self.player1.points == self.player2.points:
            return "Deuce"
        elif (self.player1.points < 4 and self.player2.points < 4) and (
            self.player1.points != self.player2.points
        ):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            return p[self.player1.points] + "-" + p[self.player2.points]
        elif self.__is_advantage_gamer__():
            return "Advantage " + self.__generate_won_player_name__()
        else:
            return "Win for " + self.__generate_won_player_name__()
