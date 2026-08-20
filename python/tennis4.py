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
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, server: Player, receiver: Player):
        self.server = server
        self.receiver = receiver

    def score(self):
        status = GameState.status(self.server, self.receiver)
        if status == GameStatus.DEUCE:
            return TennisResultFormatter.format("Deuce", "")
        if status == GameStatus.SERVER_WIN:
            return TennisResultFormatter.format("Win for " + self.server.name, "")
        if status == GameStatus.RECEIVER_WIN:
            return TennisResultFormatter.format("Win for " + self.receiver.name, "")
        if status == GameStatus.SERVER_ADVANTAGE:
            return TennisResultFormatter.format("Advantage " + self.server.name, "")
        if status == GameStatus.RECEIVER_ADVANTAGE:
            return TennisResultFormatter.format("Advantage " + self.receiver.name, "")
        if status == GameStatus.REGULAR:
            return TennisResultFormatter.format(
                self.SCORES[self.server.points], self.SCORES[self.receiver.points]
            )


class GameState:
    @staticmethod
    def status(server: Player, receiver: Player) -> GameStatus:
        s, r = server.points, receiver.points
        diff = s - r

        # Победа
        if s >= 4 and diff >= 2:
            return GameStatus.SERVER_WIN
        if r >= 4 and diff <= -2:
            return GameStatus.RECEIVER_WIN

        # Преимущество (только при diff == 1 или -1 и минимум 4 очка у лидера)
        if s >= 4 and diff == 1:
            return GameStatus.SERVER_ADVANTAGE
        if r >= 4 and diff == -1:
            return GameStatus.RECEIVER_ADVANTAGE

        # Деусе (равно и >= 3)
        if s == r and s >= 3:
            return GameStatus.DEUCE

        return GameStatus.REGULAR


class TennisResultFormatter:
    @staticmethod
    def format(server_result: str, receiver_result: str) -> str:
        if not receiver_result:
            return server_result
        if server_result == receiver_result:
            return f"{server_result}-All"
        return f"{server_result}-{receiver_result}"
