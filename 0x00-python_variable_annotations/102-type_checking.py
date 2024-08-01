#!/usr/bin/env python3
"""
Creates multiple copies of items in a tuple.
"""
from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Creates a zoomed-in version of a tuple by repeating its elements.

    Args:
        lst (Tuple[int, ...]): The tuple to zoom in on.
        factor (int): The zoom factor. Defaults to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
