def get_combinations_with_replacement_through_range(max_num: int) -> list[list[int]]:
    return [[i, j] for i in range(max_num + 1) for j in range(i, max_num + 1)]

def get_identity_pairs(min_num: int, max_num: int) -> list[list[int]]:
    return [[i, i] for i in range(min_num, max_num + 1)]
