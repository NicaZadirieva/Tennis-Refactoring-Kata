from player import Player


class TennisGame4:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, server: Player, receiver: Player):
        self.server = server
        self.receiver = receiver

    def score(self):
        if Deuce.is_deuce(self.server, self.receiver):
            return TennisResultFormatter.format("Deuce", "")
        if GameServer.server_has_won(self.server, self.receiver):
            return TennisResultFormatter.format("Win for " + self.server.name, "")
        if GameReceiver.receiver_has_won(self.server, self.receiver):
            return TennisResultFormatter.format("Win for " + self.receiver.name, "")
        if AdvantageServer.server_has_advantage(self.server, self.receiver):
            return TennisResultFormatter.format("Advantage " + self.server.name, "")
        if AdvantageReceiver.receiver_has_advantage(self.server, self.receiver):
            return TennisResultFormatter.format("Advantage " + self.receiver.name, "")

        return TennisResultFormatter.format(
            self.SCORES[self.server.points], self.SCORES[self.receiver.points]
        )


class TennisResultFormatter:
    @staticmethod
    def format(server_result: str, receiver_result: str):
        if receiver_result == "":
            return server_result
        if server_result == receiver_result:
            return server_result + "-All"
        return server_result + "-" + receiver_result


class Deuce:
    @staticmethod
    def is_deuce(server: Player, receiver: Player):
        return (
            server.points >= 3
            and receiver.points >= 3
            and (server.points == receiver.points)
        )


class GameServer:
    @staticmethod
    def server_has_won(server: Player, receiver: Player):
        return server.points >= 4 and (server.points - receiver.points) >= 2


class GameReceiver:
    @staticmethod
    def receiver_has_won(server: Player, receiver: Player):
        return receiver.points >= 4 and (receiver.points - server.points) >= 2


class AdvantageServer:
    @staticmethod
    def server_has_advantage(server: Player, receiver: Player):
        return server.points >= 4 and (server.points - receiver.points) == 1


class AdvantageReceiver:
    @staticmethod
    def receiver_has_advantage(server: Player, receiver: Player):
        return receiver.points >= 4 and (receiver.points - server.points) == 1


class DefaultResult:
    def __init__(self, game):
        self.game = game
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def get_result(self):
        return TennisResult(
            self.scores[self.game.server_score], self.scores[self.game.receiver_score]
        )
