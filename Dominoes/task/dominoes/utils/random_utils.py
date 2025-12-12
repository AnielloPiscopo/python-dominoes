import random
from typing import MutableSequence, TypeVar

T = TypeVar("T")

def get_rnd_num_in_range(min: int, max: int) -> int:
    return random.randint(min, max)

def get_rnd_values_from_mutable_sequence(
    mt_sequence: MutableSequence[T],
    num_of_values_to_get: int
) -> MutableSequence[T]:
    picked_values: MutableSequence[T] = []

    for _ in range(num_of_values_to_get):
        i = random.randrange(len(mt_sequence))
        picked_values.append(mt_sequence.pop(i))

    return picked_values
