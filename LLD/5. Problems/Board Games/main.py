import time

from engine.GameManager import GameManager
from games.SnakesNLadder.manager import SnakesNLadderGameManager
from games.TTT.game import TicTacToeGame
from games.TTT.manager import TicTacToeGameManager
from games.TTT.move import TicTacToeMove
from games.commons.move import Move
from games.commons.stats_service import StatsService
from models.Player import Player


def main():
    p1 = Player(1, "Tarush")
    p2 = Player(2, "Dev")
    p3 = Player(3, "Shash")
    tt_game = TicTacToeGameManager()
    tt_game.new_game()
    tt_game.add_player(p1)
    tt_game.add_player(p2)
    tt_game.start_game()
    tt_game.move(TicTacToeMove(p1.id, 0, 0))
    tt_game.move(TicTacToeMove(p2.id, 0, 1))
    tt_game.move(TicTacToeMove(p1.id, 0, 2))
    tt_game.move(TicTacToeMove(p2.id, 1, 1))
    tt_game.move(TicTacToeMove(p1.id, 2, 0))
    tt_game.move(TicTacToeMove(p2.id, 2, 1))
    # tt_game.move(TicTacToeMove(p1.id, 0, 2))
    tt_game.new_game()
    tt_game.add_player(p1)
    tt_game.add_player(p3)
    tt_game.start_game()
    tt_game.move(TicTacToeMove(p1.id, 0, 0))
    tt_game.move(TicTacToeMove(p3.id, 1, 1))
    tt_game.move(TicTacToeMove(p1.id, 2, 2))
    tt_game.move(TicTacToeMove(p3.id, 0, 2))
    tt_game.move(TicTacToeMove(p1.id, 0, 1))
    tt_game.move(TicTacToeMove(p3.id, 1, 0))
    tt_game.move(TicTacToeMove(p1.id, 1, 2))
    tt_game.move(TicTacToeMove(p3.id, 2, 1))
    tt_game.move(TicTacToeMove(p1.id, 2, 0))

    tt_game.display_game_stats(1)
    tt_game.display_game_stats(2)
    tt_game.display_player_stats(1)
    tt_game.display_player_stats(2)
    tt_game.display_player_stats(3)

    snl_game = SnakesNLadderGameManager()
    snl_game.new_game()
    snl_game.add_player(p1)
    snl_game.add_player(p2)
    snl_game.add_player(p3)
    snl_game.start_game()
    while not snl_game.game_completed():
        player = snl_game.next_move()
        move = snl_game.create_move(player)
        snl_game.move(move)
        time.sleep(0.1)

    snl_game.display_player_stats(1)
    snl_game.display_player_stats(2)

    StatsService.display_player_all_stats(1)


if __name__ == "__main__":
    main()
