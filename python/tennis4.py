from enum import Enum, auto

from player import Player


class GameStatus(Enum):
    REGULAR = auto()
    DEUCE = auto()
    SERVER_ADVANTAGE = auto()
    RECEIVER_ADVANTAGE = auto()
    SERVER_WIN = auto()
    RECEIVER_WIN = auto()


class TennisGame4:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, server: Player, receiver: Player):
        self.server = server
        self.receiver = receiver

    def score(self) -> str:
        """Главный метод — возвращает строку счёта"""
        status = self._determine_status()

        status_handlers = {
            GameStatus.DEUCE: self._format_deuce,
            GameStatus.SERVER_WIN: self._format_win,
            GameStatus.RECEIVER_WIN: self._format_win,
            GameStatus.SERVER_ADVANTAGE: self._format_advantage,
            GameStatus.RECEIVER_ADVANTAGE: self._format_advantage,
            GameStatus.REGULAR: self._format_regular,
        }

        handler = status_handlers.get(status)
        return handler(status) if handler else "Unknown score"

    def _determine_status(self) -> GameStatus:
        """Определяет статус игры"""
        s = self.server.points
        r = self.receiver.points
        diff = s - r

        # Проверяем победу (самые важные условия)
        if s >= 4 and diff >= 2:
            return GameStatus.SERVER_WIN
        if r >= 4 and diff <= -2:
            return GameStatus.RECEIVER_WIN

        # Проверяем преимущество (только при 4+ очках у лидера)
        if s >= 4 and diff == 1:
            return GameStatus.SERVER_ADVANTAGE
        if r >= 4 and diff == -1:
            return GameStatus.RECEIVER_ADVANTAGE

        # Делюс (равно и >= 3)
        if s == r and s >= 3:
            return GameStatus.DEUCE

        return GameStatus.REGULAR

    def _format_deuce(self, _status) -> str:
        return "Deuce"

    def _format_win(self, status: GameStatus) -> str:
        winner = (
            self.server.name if status == GameStatus.SERVER_WIN else self.receiver.name
        )
        return f"Win for {winner}"

    def _format_advantage(self, status: GameStatus) -> str:
        player = (
            self.server.name
            if status == GameStatus.SERVER_ADVANTAGE
            else self.receiver.name
        )
        return f"Advantage {player}"

    def _format_regular(self, _status) -> str:
        server_score = self.SCORE_NAMES[self.server.points]
        receiver_score = self.SCORE_NAMES[self.receiver.points]

        if server_score == receiver_score:
            return f"{server_score}-All"
        return f"{server_score}-{receiver_score}"
