from typing import Optional
from enums.enums import PlayerKind
from models.models import DominoGameState , Player
from utils.cli_utils import print_el_of_iterable_in_row
from utils.iter_utils import get_joined_str

def print_player_pieces(player_pieces:list[list[int]]):
    print("Your pieces:")
    print_el_of_iterable_in_row(player_pieces)

def print_turn_info(game_state:DominoGameState)->None:
    stock_pieces, computer_pieces, player_pieces, domino_snake, current_player , _ = game_state
    stock_pieces: list[list[int]]
    computer_pieces: list[list[int]]
    player_pieces: list[list[int]]
    domino_snake: list[list[int]]
    current_player: Player

    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()
    print_domino_snake(domino_snake)
    print()
    print_player_pieces(player_pieces)
    print()
    print_current_status(current_player.kind)

def print_domino_snake(domino_snake:list[list[int]])->None:
    domino_snake_str:str = get_joined_str(domino_snake , "")

    if len(domino_snake) <= 6:
        print(domino_snake_str)
    else:
        print(
            f"{get_joined_str(domino_snake[:3],"")}...{get_joined_str(domino_snake[-3:],"")}"
        )

def print_current_status(current_player_kind:PlayerKind)->None:
    if current_player_kind == PlayerKind.PLAYER:
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()

def print_winner(winner:Optional[Player])->None:
    if winner is None:
        print("Status: The game is over. It's a draw!")
    elif winner.kind == PlayerKind.PLAYER:
        print("Status: The game is over. You won!")
    elif winner.kind == PlayerKind.COMPUTER:
        print("Status: The game is over. The computer won!")
