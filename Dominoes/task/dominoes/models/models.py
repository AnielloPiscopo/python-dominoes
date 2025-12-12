from typing import NamedTuple, Optional
from enums.enums import PlayerKind

class Player(NamedTuple):
    kind:PlayerKind

class DominoGameState(NamedTuple):
    stock_pieces: list[list[int]]
    computer_pieces: list[list[int]]
    player_pieces: list[list[int]]
    domino_snake: list[list[int]]
    current_player: Player
    winner:Optional[Player] = None