from player import Player


class TennisGame4:
    SCORES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, server: Player, receiver: Player):
        self.server = server
        self.receiver = receiver

    def score(self):
        if Deuce.is_deuce(self.server, self.receiver):
            return TennisResult("Deuce", "").format()
        if GameServer.server_has_won(self.server, self.receiver):
            return TennisResult("Win for " + self.server.name, "").format()
        if GameReceiver.receiver_has_won(self.server, self.receiver):
            return TennisResult("Win for " + self.receiver.name, "").format()
        if AdvantageServer.server_has_advantage(self.server, self.receiver):
            return TennisResult("Advantage " + self.server.name, "").format()
        if AdvantageReceiver.receiver_has_advantage(self.server, self.receiver):
            return TennisResult("Advantage " + self.receiver.name, "").format()

        return TennisResult(
            self.SCORES[self.server.points], self.SCORES[self.receiver.points]
        ).format()


class TennisResult:
    def __init__(self, server_score, receiver_score):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def format(self):
        if "" == self.receiver_score:
            return self.server_score
        if self.server_score == self.receiver_score:
            return self.server_score + "-All"
        return self.server_score + "-" + self.receiver_score


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
