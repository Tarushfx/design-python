from games.TTT.game import TicTacToeGame
from games.TTT.manager import TicTacToeGameManager
from games.TTT.move import TicTacToeMove
from games.commons.move import Move
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
    tt_game.move(TicTacToeMove(p1.id, 2, 0))
    tt_game.move(TicTacToeMove(p3.id, 0, 1))
    tt_game.move(TicTacToeMove(p1.id, 0, 2))
    tt_game.move(TicTacToeMove(p3.id, 2, 1))
    tt_game.move(TicTacToeMove(p1.id, 0, 2))
    tt_game.move(TicTacToeMove(p3.id, 0, 1))

    tt_game.display_game_stats(1)
    tt_game.display_game_stats(2)
    tt_game.display_player_stats(1)
    tt_game.display_player_stats(2)
    tt_game.display_player_stats(3)


if __name__ == "__main__":
    main()
