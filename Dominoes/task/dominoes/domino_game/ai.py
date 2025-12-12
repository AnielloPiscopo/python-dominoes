from exceptions.exceptions import IllegalMoveError
from utils.iter_utils import get_flatten_iterable,get_values_with_counts,sort_by_score_desc
from domino_game.engine import apply_move , take_piece_from_stock

def play_turn_as_computer(computer_pieces:list[list[int]] , stock_pieces:list[list[int]] , domino_snake:list[list[int]])->None:
    pieces_with_potential_scores: list[tuple[list[int], int]] = get_pieces_with_potential_scores(computer_pieces,
                                                                                             domino_snake)
    if not has_computer_moved_own_piece(pieces_with_potential_scores , computer_pieces , domino_snake):
        take_piece_from_stock(stock_pieces , computer_pieces)


def has_computer_moved_own_piece(pieces_with_potential_scores: list[tuple[list[int], int]],
                                 computer_pieces:list[list[int]], domino_snake:list[list[int]])->bool:
    for piece, score in pieces_with_potential_scores:
        try:
            piece_index: int = computer_pieces.index(piece)

            right_move: bool = try_apply_move(piece, piece_index, computer_pieces, domino_snake, True)
            if right_move:
                return True

            left_move: bool = try_apply_move(piece, piece_index, computer_pieces, domino_snake, False)
            if left_move:
                return True
        except (IllegalMoveError, ValueError):
            continue

    return False

def try_apply_move(
    piece: list[int],
    piece_index: int,
    current_pieces: list[list[int]],
    domino_snake: list[list[int]],
    is_positive_move: bool
) -> bool:
    try:
        apply_move(piece, piece_index, current_pieces, domino_snake, is_positive_move)
        return True
    except IllegalMoveError:
        return False

def get_pieces_with_potential_scores(computer_pieces:list[list[int]], domino_snake:list[list[int]]) -> list[tuple[list[int] , int]]:
    nums_with_occurrences:list[tuple[int , int]] = (
        get_values_with_counts(get_flatten_iterable(computer_pieces) + get_flatten_iterable(domino_snake)))

    pieces_with_potential_scores:list[tuple[list[int] , int]] = list()

    for piece in computer_pieces:
        pieces_with_potential_scores.append(get_piece_with_potential_score(piece, nums_with_occurrences))

    return list(sort_by_score_desc(pieces_with_potential_scores , lambda x: x[1]))

def get_piece_with_potential_score(piece:list[int], nums_with_occurrences:list[tuple[int , int]])->tuple[list[int] , int]:
    potential_score: int = 0

    for num in piece:
        potential_score += next((v for k, v in nums_with_occurrences if k == num), None)

    return piece , potential_score


