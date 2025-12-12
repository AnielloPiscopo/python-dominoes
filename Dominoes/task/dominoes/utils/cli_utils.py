from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")

def print_el_of_iterable_in_row(seq: Iterable[T], start_counter: int = 1) -> None:
    for i, el in enumerate(seq, start=start_counter):
        print(f"{i}:{el}")

def get_num() -> int:
    try:
        num: int = int(input().strip())
        return num
    except ValueError:
        raise ValueError("The value must be an integer")

def get_num_in_range(min: int, max: int, is_min_included: bool, is_max_included: bool) -> int:
    while True:
        error_msg: str = "The value must be in range between "

        num: int = get_num()

        if is_min_included and is_max_included:
            if max >= num >= min:
                return num
            else:
                raise ValueError(f"{error_msg} {min} and {max} both included")
        elif is_min_included:
            if max > num >= min:
                return num
            else:
                raise ValueError(f"{error_msg} {min}(included) and {max}(excluded)")
        elif is_max_included:
            if max >= num > min:
                return num
            else:
                raise ValueError(f"{error_msg} {min}(excluded) and {max}(included)")
        else:
            if max > num > min:
                return num
            else:
                raise ValueError(f"{error_msg} {min} and {max} both excluded")
