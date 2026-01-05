from games.TTT.game import TicTacToeGame
from games.TTT.move import TicTacToeMove
from engine.GameManager import GameManager


class TicTacToeGameManager(GameManager):
    game_count = 1

    # TODO make it singleton
    def __init__(self):
        super().__init__(self.game_count)
        self.sign_to_player = None
        self.player_signs = None

    def start_game(self):
        if len(self.players) < self.min_players:
            print("Not enough players")
            return
        self.game = TicTacToeGame(self.game_count, self.players)
        self.set_game(self.game)
        print(f"Game {self.id} Initialized")
        self.set_player_signs()
        self.game_count += 1

    def set_players(self, players):
        self.players = players

    def add_player(self, player):
        if len(self.players) >= self.max_players:
            print("Too many players")
            return
        self.players.append(player)
        print(f"Player {player.id} added to game {self.id}")

    def set_player_signs(self):
        self.sign_to_player = {}
        self.player_signs = {}
        for player, sign in zip(self.game.get_player_list(), self.game.signs):
            self.sign_to_player[sign] = player
            self.player_signs[player] = sign

    def __end_game(self):
        print("Game Ended")
        winners = self.calculate_winners()
        players = self.game.get_player_list()
        losers = list(set(players) - set(winners))
        print(f"{"".join(map(str, winners))} Wins game {self.game.id}!")
        print(f"{"".join(map(str, losers))} Loses game {self.game.id}!")
        # TODO add to stats here
        pass

    def calculate_winners(self):
        winner_move = self.game.get_winner()
        return [self.sign_to_player[winner_move]]

    def move(self, move: TicTacToeMove):
        move.set_sign(self.player_signs[move.player])
        if self.game.is_complete():
            print(f"Invalid Move. Game {self.game.id} has ended")
            return
        if self.game.is_valid_move(move):
            self.game.make_move(move)
            print(f"Player {move.player} moved {move.sign} at {move.row}x{move.col}")
            self.game.board.print_board()
            if self.game.is_complete():
                self.__end_game()
        else:
            print("Invalid Move.")
