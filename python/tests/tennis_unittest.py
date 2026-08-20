import unittest

from player import Player
from tennis1 import TennisGame1
from tennis2 import TennisGame2
from tennis3 import TennisGame3
from tennis4 import TennisGame4
from tennis5 import TennisGame5
from tennis6 import TennisGame6
from tennis7 import TennisGame7

test_cases = [
    (0, 0, "Love-All", "player1", "player2"),
    (1, 1, "Fifteen-All", "player1", "player2"),
    (2, 2, "Thirty-All", "player1", "player2"),
    (3, 3, "Deuce", "player1", "player2"),
    (4, 4, "Deuce", "player1", "player2"),
    (1, 0, "Fifteen-Love", "player1", "player2"),
    (0, 1, "Love-Fifteen", "player1", "player2"),
    (2, 0, "Thirty-Love", "player1", "player2"),
    (0, 2, "Love-Thirty", "player1", "player2"),
    (3, 0, "Forty-Love", "player1", "player2"),
    (0, 3, "Love-Forty", "player1", "player2"),
    (4, 0, "Win for player1", "player1", "player2"),
    (0, 4, "Win for player2", "player1", "player2"),
    (2, 1, "Thirty-Fifteen", "player1", "player2"),
    (1, 2, "Fifteen-Thirty", "player1", "player2"),
    (3, 1, "Forty-Fifteen", "player1", "player2"),
    (1, 3, "Fifteen-Forty", "player1", "player2"),
    (4, 1, "Win for player1", "player1", "player2"),
    (1, 4, "Win for player2", "player1", "player2"),
    (3, 2, "Forty-Thirty", "player1", "player2"),
    (2, 3, "Thirty-Forty", "player1", "player2"),
    (4, 2, "Win for player1", "player1", "player2"),
    (2, 4, "Win for player2", "player1", "player2"),
    (4, 3, "Advantage player1", "player1", "player2"),
    (3, 4, "Advantage player2", "player1", "player2"),
    (5, 4, "Advantage player1", "player1", "player2"),
    (4, 5, "Advantage player2", "player1", "player2"),
    (15, 14, "Advantage player1", "player1", "player2"),
    (14, 15, "Advantage player2", "player1", "player2"),
    (6, 4, "Win for player1", "player1", "player2"),
    (4, 6, "Win for player2", "player1", "player2"),
    (16, 14, "Win for player1", "player1", "player2"),
    (14, 16, "Win for player2", "player1", "player2"),
]


def play_game(TennisGame, p1_points, p2_points, p1_name, p2_name):
    game = TennisGame(p1_name, p2_name)
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.won_point(p1_name)
        if i < p2_points:
            game.won_point(p2_name)
    return game


def play_game1(TennisGame1, player1, player2):
    game = TennisGame1(player1, player2)
    old_point1 = game.player1.points
    old_point2 = game.player2.points
    new_point1 = 0
    new_point2 = 0
    for i in range(max(old_point1, old_point2)):
        if i < old_point1:
            new_point1 += 1
        if i < old_point2:
            new_point2 += 1
    game.player1.points = new_point1
    game.player2.points = new_point2
    return game


def play_game4(TennisGame4, player1, player2):
    game = TennisGame4(player1, player2)
    old_point1 = game.server.points
    old_point2 = game.receiver.points
    new_point1 = 0
    new_point2 = 0
    for i in range(max(old_point1, old_point2)):
        if i < old_point1:
            new_point1 += 1
        if i < old_point2:
            new_point2 += 1
    game.server.points = new_point1
    game.receiver.points = new_point2
    return game


class TestTennis(unittest.TestCase):
    def test_score_game1(self):
        for testcase in test_cases:
            (p1_points, p2_points, score, p1_name, p2_name) = testcase
            player1 = Player(p1_name, p1_points)
            player2 = Player(p2_name, p2_points)
            game = play_game1(TennisGame1, player1, player2)
            with self.subTest(f"{TennisGame1.__name__} - {testcase}"):
                self.assertEqual(score, game.score())

    def test_score_game2(self):
        for testcase in test_cases:
            (p1_points, p2_points, score, p1_name, p2_name) = testcase
            player1 = Player(p1_name, p1_points)
            player2 = Player(p2_name, p2_points)
            game = play_game1(TennisGame2, player1, player2)
            with self.subTest(f"{TennisGame2.__name__} - {testcase}"):
                self.assertEqual(score, game.score())

    def test_score_game3(self):
        for testcase in test_cases:
            (p1_points, p2_points, score, p1_name, p2_name) = testcase
            player1 = Player(p1_name, p1_points)
            player2 = Player(p2_name, p2_points)
            game = play_game1(TennisGame3, player1, player2)
            with self.subTest(f"{TennisGame3.__name__} - {testcase}"):
                self.assertEqual(score, game.score())

    def test_score_game4(self):
        for testcase in test_cases:
            (p1_points, p2_points, score, p1_name, p2_name) = testcase
            player1 = Player(p1_name, p1_points)
            player2 = Player(p2_name, p2_points)
            game = play_game1(TennisGame4, player1, player2)
            with self.subTest(f"{TennisGame4.__name__} - {testcase}"):
                self.assertEqual(score, game.score())

    def test_score_games_4_thru_6(self):
        for TennisGameClass in (
            TennisGame5,
            TennisGame6,
        ):
            for testcase in test_cases:
                (p1_points, p2_points, score, p1_name, p2_name) = testcase
                game = play_game(
                    TennisGameClass, p1_points, p2_points, p1_name, p2_name
                )
                with self.subTest(f"{TennisGameClass.__name__} - {testcase}"):
                    self.assertEqual(score, game.score())

    def test_score_game7(self):
        for testcase in test_cases:
            (p1_points, p2_points, score, p1_name, p2_name) = testcase
            game = play_game(TennisGame7, p1_points, p2_points, p1_name, p2_name)
            with self.subTest(f"{TennisGame7.__name__} - {testcase}"):
                self.assertEqual(
                    "Current score: " + score + ", enjoy your game!",
                    game.score(),
                )


if __name__ == "__main__":
    unittest.main()
