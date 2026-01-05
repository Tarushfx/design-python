from dataclasses import dataclass
from typing import List


@dataclass
class GameResult:
    id: int
    players: List[int] = None
    winner_player: List[int] = None
    loser_player: List[int] = None
