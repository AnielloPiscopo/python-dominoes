from enums.enums import PlayerKind
from models.models import DominoGameState , Player
from exceptions.exceptions import IllegalMoveError
from domino_game.ai import play_turn_as_computer
from domino_game.engine import apply_player_move , check_game_over
from domino_game.setup import set_up
from domino_game.io import print_winner , print_turn_info
from utils.cli_utils import get_num_in_range

def play_turn(game_state:DominoGameState)->DominoGameState:
    stock_pieces, computer_pieces, player_pieces, domino_snake, current_player , _ = game_state
    stock_pieces: list[list[int]]
    computer_pieces: list[list[int]]
    player_pieces: list[list[int]]
    domino_snake: list[list[int]]
    current_player: Player

    if current_player.kind == PlayerKind.PLAYER:
        play_turn_as_player(player_pieces , stock_pieces , domino_snake)
        game_state = game_state._replace(current_player=Player(PlayerKind.COMPUTER))
    else:
        play_turn_as_computer(computer_pieces , stock_pieces , domino_snake)
        game_state = game_state._replace(current_player=Player(PlayerKind.PLAYER))

    return game_state

def play_turn_as_player(player_pieces:list[list[int]] , stock_pieces:list[list[int]] , domino_snake:list[list[int]])->None:
    while True:
        try:
            player_num: int = get_num_in_range(-len(player_pieces), len(player_pieces), True, True)
            apply_player_move(player_num, player_pieces, stock_pieces, domino_snake)
            break
        except IllegalMoveError:
            print("Illegal move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def play()->None:
    game_state:DominoGameState = set_up()
    start_game(game_state)

def start_game(
        game_state:DominoGameState
)->None:
    while True:
        print_turn_info(game_state)
        game_state = play_turn(game_state)

        is_game_over , game_state = check_game_over(game_state)
        is_game_over:bool
        game_state:DominoGameState

        if is_game_over:
            break

    print_turn_info(game_state)
    print_winner(game_state.winner)