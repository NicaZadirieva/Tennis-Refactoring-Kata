from player import Player


class TennisGame1:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def create_deuce_phrase(self, player: Player):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(player.points, "Deuce")

    def create_advantage_phrase(self, player1: Player, player2: Player):
        expression = player1.points - player2.points
        return {1: "Advantage player1", -1: "Advantage player2"}.get(expression)

    def create_won_phrase(self, player1: Player, player2: Player):
        expression = player1.points - player2.points
        if expression >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def additional_phrase_for(self, player: Player):
        additional_phrase_dict = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        return additional_phrase_dict.get(player.points, "")

    def score(self):
        result = ""
        if self.player1.points == self.player2.points:
            result = self.create_deuce_phrase(self.player1)
        elif self.player1.points >= 4 or self.player2.points >= 4:
            advantage_phrase = self.create_advantage_phrase(self.player1, self.player2)
            if advantage_phrase is None:
                won_phrase = self.create_won_phrase(self.player1, self.player2)
                result = won_phrase
            else:
                result = advantage_phrase
        else:
            result += self.additional_phrase_for(self.player1)
            result += "-"
            result += self.additional_phrase_for(self.player2)
        return result
