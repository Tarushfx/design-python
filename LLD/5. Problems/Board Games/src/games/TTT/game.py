from engine.Game import Game
from games.TTT.board import TicTacToeBoard
from games.TTT.move import TicTacToeMove


class TicTacToeGame(Game):
    def __init__(self, id, players):
        super().__init__(id)
        self.initialize()
        self.last_mover = None
        self.completed = False
        self.winner = None
        self.signs = ["O", "X"]
        self.current_move = self.signs[0]
        self.set_player_list(players)
        self.winner_player = None
        self.loser_player = None

    def flip_move(self):
        self.current_move = self.signs[self.current_move == self.signs[0]]

    def is_complete(self):
        size = self.board.size()
        for row in range(size):
            flag = True
            start = self.board.get_position(row, 0)
            if not start:
                continue
            for col in range(size):
                if self.board.get_position(row, col) != start:
                    flag = False
                    break
            if flag:
                self.set_winner(start)
                return flag
        for col in range(size):
            flag = True
            start = self.board.get_position(0, col)
            if not start:
                continue

            for row in range(size):
                if self.board.get_position(row, col) != start:
                    flag = False
                    break
            if flag:
                self.set_winner(start)
                return flag
        flag = True
        start = self.board.get_position(0, 0)
        if start:
            for col in range(size):
                if self.board.get_position(col, col) != start:
                    flag = False
                    break
            if flag:
                self.set_winner(start)
                return flag
        flag = True
        start = self.board.get_position(0, 2)
        if start:
            for row in range(size):
                if self.board.get_position(row, size - 1 - row) != start:
                    flag = False
                    break
            if flag:
                self.set_winner(start)
                return flag
        flag = True
        for row in range(size):
            for col in range(size):
                if not self.board.is_position_filled(row, col):
                    flag = False
        if flag:
            self.game_draw()
            return True
        return False

    def set_winner(self, winner):
        self.mark_complete()
        self.winner = winner

    def game_draw(self):
        self.mark_complete()

    def mark_complete(self):
        self.completed = True

    def get_winner(self):
        if not self.completed:
            return None
        return self.winner

    def is_valid_move(self, move: TicTacToeMove):
        if move.player == self.last_mover:
            print("Wrong player played the move")
            return False
        if self.current_move != move.sign:
            print("Wrong symbol")
            return False
        if self.board.is_position_filled(move.row, move.col):
            print("Position already filled")
            return False
        print("Valid move")
        return True

    def initialize(self):
        self.board = TicTacToeBoard()
        print("TTT Board created")

    def make_move(self, move):
        self.board.place(move.row, move.col, move.sign)
        self.flip_move()
        self.last_mover = move.player
