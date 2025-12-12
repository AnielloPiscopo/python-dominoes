from enums.enums import PlayerKind
from models.models import DominoGameState , Player
from exceptions.exceptions import IllegalMoveError
from utils.iter_utils import count_occurrences , get_flatten_iterable

def apply_player_move(move:int, player_pieces:list[list[int]], stock_pieces:list[list[int]],
                      domino_snake:list[list[int]]) -> None:
    if move == 0:
        take_piece_from_stock(stock_pieces , player_pieces)
        return

    is_positive_move:bool = move>0
    chosen_piece_index:int = abs(move) -1
    chosen_piece: list[int] = player_pieces[chosen_piece_index]

    apply_move(chosen_piece, chosen_piece_index, player_pieces, domino_snake, is_positive_move)

def take_piece_from_stock(stock_pieces:list[list[int]] , current_pieces:list[list[int]]) -> None:
    if stock_pieces:
        current_pieces.append(stock_pieces.pop(0))

def apply_move(piece:list[int] ,piece_index:int, current_pieces:list[list[int]] ,domino_snake:list[list[int]],
               is_positive_move:bool)->None:
    if is_positive_move:
        chosen_piece = get_piece_after_move_validation(piece, domino_snake[-1][1] , True)
        current_pieces.pop(piece_index)
        domino_snake.append(chosen_piece)
    else:
        chosen_piece = get_piece_after_move_validation(piece, domino_snake[0][0] , False)
        current_pieces.pop(piece_index)
        domino_snake.insert(0,chosen_piece)

def get_piece_after_move_validation(piece:list[int], num_to_compare:int , is_positive_move:bool)->list[int]:
    try:
        piece_num_index:int = piece.index(num_to_compare)
    except ValueError:
        raise IllegalMoveError()

    if is_positive_move:
        if piece_num_index == 0:
            return piece
        else:
            return piece[::-1]
    else:
        if piece_num_index == 0:
            return piece[::-1]
        else:
            return piece


def check_game_over(game_state:DominoGameState)->tuple[bool,DominoGameState]:
    stock_pieces, computer_pieces, player_pieces, domino_snake, current_player,winner = game_state
    stock_pieces: list[list[int]]
    computer_pieces: list[list[int]]
    player_pieces: list[list[int]]
    domino_snake: list[list[int]]
    current_player: Player
    winner:Player

    if len(player_pieces) == 0:
        game_state = game_state._replace(winner=Player(PlayerKind.PLAYER))
        return True,game_state
    elif len(computer_pieces) == 0:
        game_state = game_state._replace(winner=Player(PlayerKind.COMPUTER))
        return True,game_state
    elif check_draw(domino_snake):
        return True,game_state
    else:
        return False,game_state

def check_draw(domino_snake:list[list[int]])->bool:
    left_num_in_domino_snake:int = domino_snake[0][0]
    right_num_in_domino_snake:int = domino_snake[-1][1]

    return True if (left_num_in_domino_snake== right_num_in_domino_snake and
        count_occurrences(get_flatten_iterable(domino_snake) , left_num_in_domino_snake)==8) else False