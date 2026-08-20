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
        # Сначала проверяем, не закончился ли гейм
        if server.points >= 4 and (server.points - receiver.points) >= 2:
            return GameStatus.SERVER_WIN
        if receiver.points >= 4 and (receiver.points - server.points) >= 2:
            return GameStatus.RECEIVER_WIN

        # Теперь проверяем преимущество (нужно минимум 4 очка и разница 1)
        if server.points >= 4 and (server.points - receiver.points) == 1:
            return GameStatus.SERVER_ADVANTAGE
        if receiver.points >= 4 and (receiver.points - server.points) == 1:
            return GameStatus.RECEIVER_ADVANTAGE

        # Деус: оба >= 3 и равны
        if (
            server.points >= 3
            and receiver.points >= 3
            and server.points == receiver.points
        ):
            return GameStatus.DEUCE

        # Обычный счёт
        return GameStatus.REGULAR


class TennisResultFormatter:
    @staticmethod
    def format(server_result: str, receiver_result: str) -> str:
        if not receiver_result:
            return server_result
        if server_result == receiver_result:
            return f"{server_result}-All"
        return f"{server_result}-{receiver_result}"
