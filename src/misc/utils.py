from typing import Any

def get_centered_start(parent: tuple[int, int], child: tuple[int, int]) -> tuple[int, int]:
    return (
        (parent[0] - child[0]) // 2,
        (parent[1] - child[1]) // 2
    )

def offset_tuple(tup: tuple[int, int], offset: tuple[int, int]) -> tuple[int, int]:
    return (tup[0] + offset[0], tup[1] + offset[1])

def offset_tuple_scalar(tup: tuple[int, int], offset: int) -> tuple[int, int]:
    return (tup[0] + offset, tup[1] + offset)

def scale_tuple(tup: tuple[int, int], factor: int) -> tuple[int, int]:
    return (tup[0] * factor, tup[1] * factor)