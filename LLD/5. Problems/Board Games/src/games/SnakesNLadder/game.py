from typing import Optional

from engine.Game import Game
from games.SnakesNLadder.board import SnakesNLadderBoard
from games.SnakesNLadder.move import SnakeNLadderMove
from games.TTT.board import TicTacToeBoard
from games.TTT.move import TicTacToeMove
import random


class SnakeNLadderGame(Game):
    def __init__(self, id, players):
        super().__init__(id)
        self.board: Optional[SnakesNLadderBoard] = None
        self.signs = ["A", "B"]
        self.positions = {}
        self.initialize()
        self.last_mover = None
        self.completed = False
        self.winner: Optional[str] = None
        self.current_move: str = self.signs[0]
        self.set_player_list(players)
        self.winner_player = None
        self.loser_player = None
        self.snake_count = 5
        self.ladder_count = 5
        self.ladders = {}
        self.snakes = {}
        self.dice = 6
        self.max_roll = 3 * self.dice - 1
        self.end_pos = self.board.size() ** 2 - 1
        self.forbidden_positions = [0, self.end_pos]
        self.generate_board_elements()

    def roll_the_die(self):
        return random.randint(1, self.dice + 1)

    def generate_board_elements(self):
        used_positions = set()
        ladders = {}
        snakes = {}
        board_size = self.board.size() ** 2

        def get_random_pair():
            pos1 = random.randint(2, board_size - 1)
            pos2 = random.randint(2, board_size - 1)

            if (
                    pos1 == pos2 or
                    pos1 in used_positions or
                    pos2 in used_positions or
                    pos1 in self.forbidden_positions or
                    pos2 in self.forbidden_positions
            ):
                return None
            return pos1, pos2

        while len(ladders) < self.ladder_count:
            pair = get_random_pair()
            if pair:
                start, end = min(pair), max(pair)
                ladders[start] = end
                used_positions.update([start, end])

        while len(snakes) < self.snake_count:
            pair = get_random_pair()
            if pair:
                start, end = max(pair), min(pair)
                snakes[start] = end
                used_positions.update([start, end])

        self.ladders = ladders
        self.snakes = snakes

    def create_move(self):
        cnt = 3
        total = 0
        for i in range(cnt):
            roll = self.roll_the_die()
            total = total + roll
            if roll != self.dice:
                break
        if total > self.max_roll:
            return 0
        return total

    def flip_move(self):
        self.current_move = self.signs[self.current_move == self.signs[0]]

    def is_complete(self):
        return any(x == self.end_pos for x in self.positions.values())

    def set_winner(self):
        self.mark_complete()
        self.winner: str = self.current_move

    def mark_complete(self):
        self.completed = True

    def get_winner(self):
        if not self.completed:
            return None
        return self.winner

    def is_valid_move(self, move: SnakeNLadderMove):
        if move.player == self.last_mover:
            print("Wrong player played the move")
            return False
        if self.current_move != move.sign:
            print("Wrong symbol")
            return False
        if move.roll > self.max_roll:
            return False
        print("Valid move")
        return True

    def initialize(self):
        self.board = SnakesNLadderBoard()
        for x in self.signs:
            self.positions[x] = 0
        print("SNL Board created")

    def position_transform(self, pos):
        size = self.board.size()
        r, c = pos // size, pos % size
        if r & 1:
            c = size - 1 - c
        return r, c

    def rev_position_transform(self, r, c):
        if r & 1:
            c = self.board.size() - 1 - c
        return r * self.board.size() + c

    def get_position(self, move: SnakeNLadderMove):
        return self.position_transform(self.positions[move.sign])

    def make_move(self, move):
        r, c = self.get_position(move)
        curr_pos = self.rev_position_transform(r, c)
        new_pos = curr_pos + move.roll
        if new_pos > self.end_pos:
            new_pos = curr_pos
        nr, nc = self.position_transform(new_pos)
        self.board.remove_from_board(r, c)
        self.board.place_on_board(nr, nc, move.sign)
        self.update_positions(move.sign, new_pos)
        print(f"Player {move.sign} placed at position {nr}x{nc}")
        self.flip_move()
        self.last_mover = move.player

    def update_positions(self, player, pos):
        self.positions[player] = pos
