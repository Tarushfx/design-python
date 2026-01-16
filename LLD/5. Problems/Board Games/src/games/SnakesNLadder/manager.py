from games.SnakesNLadder.game import SnakeNLadderGame
from games.SnakesNLadder.move import SnakeNLadderMove
from games.SnakesNLadder.stats import SnakesNLadderStats
from games.TTT.game import TicTacToeGame
from games.TTT.move import TicTacToeMove
from engine.GameManager import GameManager
from games.TTT.stats import TicTacToeStats
from games.commons.stats_service import StatsService


class SnakesNLadderGameManager(GameManager):
    game_count = 0
    current_mover = 0

    def __init__(self):
        super().__init__(self.game_count)
        self.sign_to_player = None
        self.player_signs = None
        self.stats_service = SnakesNLadderStats()
        print("SnakesNLadderGameManager initialized")

    def new_game(self):
        self.game_count += 1
        self.clear()

    def create_move(self, player):
        sign = self.player_signs[player]
        move = SnakeNLadderMove(
            player=player,
            val=self.game.create_move()
        )
        move.set_sign(sign)
        return move

    def start_game(self):
        if len(self.players) < self.min_players:
            print("Not enough players")
            return
        self.game = SnakeNLadderGame(self.game_count, self.players)
        self.set_game(self.game)
        print(f"Game {self.id} Initialized")
        self.set_player_signs()

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
        losers = list(set(players) - set(winners)) if winners else []
        if winners:
            print(f"{" ".join(map(str, winners))} Wins game {self.game.id}!")
            print(f"{" ".join(map(str, losers))} Loses game {self.game.id}!")
        else:
            print(f"Game {self.game.id} drawn")
        self.game.winner_player = winners
        self.game.loser_player = losers
        self.stats_service.record_game(self.game)
        self.clear()

    def calculate_winners(self):
        winner_move = self.game.get_winner()
        if not winner_move:
            return []
        return [self.sign_to_player[winner_move]]

    def game_completed(self):
        return self.game.is_complete()

    def flip_move(self):
        self.current_mover = (self.current_mover + 1) % len(self.players)

    def move(self, move: SnakeNLadderMove):
        if self.game.is_complete():
            print(f"Invalid Move. Game {self.game.id} has ended")
            return
        move.set_sign(self.player_signs[move.player])
        if self.game.is_valid_move(move):
            print(f"Player {move.player} {move.sign} moved {move.roll}")
            self.game.make_move(move)
            self.flip_move()
            if self.game.is_complete():
                self.game.set_winner()
                self.game.board.print_board()
                self.__end_game()
        else:
            print("Invalid Move.")

    def display_game_stats(self, game_id):
        self.stats_service.display_game_stats(game_id)

    def display_player_stats(self, player_id):
        self.stats_service.display_player_stats(player_id)

    def clear(self):
        self.sign_to_player = None
        self.player_signs = None
        self.players = []

    def next_move(self):
        players = self.game.get_player_list()
        return players[self.current_mover]
