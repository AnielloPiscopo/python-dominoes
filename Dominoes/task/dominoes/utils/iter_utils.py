from collections.abc import Iterable
from typing import Sequence , Callable , TypeVar , Optional
from collections import Counter

T = TypeVar("T")

def get_first_common(seq_to_check: Iterable[T], seq_to_compare: Iterable[T]) -> Optional[T]:
    return next((x for x in seq_to_check if x in seq_to_compare), None)

def count_occurrences(iterable: Iterable[T], value: T) -> int:
    return sum(1 for el in iterable if el == value)

def get_flatten_iterable(nested: Iterable[Iterable[T]]) -> list[T]:
    return [item for inner in nested for item in inner]

def get_joined_str(seq: Sequence[Sequence[int]], str_for_join: str) -> str:
    return str_for_join.join(str(el) for el in seq)

def get_values_with_counts(iterable: Iterable[T]) -> list[tuple[T, int]]:
    counter = Counter(iterable)
    return counter.most_common()

def sort_by_score_desc(
    items: Iterable[T],
    score_getter: Callable[[T], int]
) -> Iterable[T]:
    return sorted(items, key=score_getter, reverse=True)
