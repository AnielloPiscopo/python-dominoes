from typing import Optional
from enums.enums import PlayerKind
from models.models import DominoGameState , Player
from utils.iter_utils import get_first_common
from utils.random_utils import get_rnd_values_from_mutable_sequence
from utils.combinatorics import get_combinations_with_replacement_through_range , get_identity_pairs

def get_domino_set(higher_num:int)->list[list[int]]:
    return get_combinations_with_replacement_through_range(higher_num)

def get_pieces(domino_set:list[list[int]])->list[list[int]]:
    return list(get_rnd_values_from_mutable_sequence(domino_set , 7))

def get_doubles(higher_num:int)->list[list[int]]:
    return sorted(get_identity_pairs(0 , higher_num) , reverse=True)

def check_doubles_presence(pieces:list[list[int]])->Optional[list[int]]:
    return get_first_common(get_doubles(6),pieces)

def get_first_pair_with_player(double_in_computer_pieces:Optional[list[int]], double_in_player_pieces:Optional[list[int]],
                               computer_pieces:list[list[int]], player_pieces:list[list[int]])->tuple[Player,list[int]]:
    player:Player

    if double_in_player_pieces is None:
        computer_pieces.remove(double_in_computer_pieces)
        return Player(PlayerKind.PLAYER), double_in_computer_pieces

    if double_in_computer_pieces is None:
        player_pieces.remove(double_in_player_pieces)
        return Player(PlayerKind.COMPUTER), double_in_player_pieces

    if double_in_computer_pieces[0] > double_in_player_pieces[0]:
        computer_pieces.remove(double_in_computer_pieces)
        return Player(PlayerKind.PLAYER),double_in_computer_pieces
    elif double_in_computer_pieces[0] < double_in_player_pieces[0]:
        player_pieces.remove(double_in_player_pieces)
        return Player(PlayerKind.COMPUTER),double_in_player_pieces

    return Player(PlayerKind.COMPUTER),[0]

def set_up()->DominoGameState:
    while True:
        stock_pieces: list[list[int]] = get_domino_set(6)
        computer_pieces: list[list[int]] = get_pieces(stock_pieces)
        player_pieces: list[list[int]] = get_pieces(stock_pieces)
        double_in_computer_pieces:Optional[list[int]] = check_doubles_presence(computer_pieces)
        double_in_player_pieces: Optional[list[int]] = check_doubles_presence(player_pieces)

        if double_in_computer_pieces or double_in_player_pieces:
            break

    current_player,first_pair = get_first_pair_with_player(double_in_computer_pieces, double_in_player_pieces, computer_pieces, player_pieces)
    current_player: Player
    first_pair: list[int]

    domino_snake:list[list[int]] = [first_pair]

    return DominoGameState(stock_pieces, computer_pieces, player_pieces, domino_snake, current_player)