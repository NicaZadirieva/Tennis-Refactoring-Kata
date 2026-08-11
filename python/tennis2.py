from player import Player


class TennisGame2:
    POINTS_TO_SCORE = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def _is_regular_score(self) -> bool:
        """Проверяет, находится ли игра в состоянии обычного счета.

        Обычный счет - это когда оба игрока набрали меньше 4 очков
        и их очки не равны (равный счет обрабатывается отдельно как Deuce).
        """
        return (
            self.player1.points < 4
            and self.player2.points < 4
            and self.player1.points != self.player2.points
        )

    def create_deuce_phrase(self, player: Player):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(player.points, "Deuce")

    def score(self):
        result = ""

        if self.player1.points == self.player2.points:
            result = self.create_deuce_phrase(self.player1)
        elif self._is_regular_score():
            result = (
                self.POINTS_TO_SCORE[self.player1.points]
                + "-"
                + self.POINTS_TO_SCORE[self.player2.points]
            )

        # Win conditions
        elif (
            self.player1.points >= 4
            and (self.player1.points - self.player2.points) >= 2
        ):
            result = "Win for player1"

        elif (
            self.player2.points >= 4
            and (self.player2.points - self.player1.points) >= 2
        ):
            result = "Win for player2"

        # Advantage conditions
        elif self.player1.points > self.player2.points and self.player2.points >= 3:
            result = "Advantage player1"

        elif self.player2.points > self.player1.points and self.player1.points >= 3:
            result = "Advantage player2"

        return result
