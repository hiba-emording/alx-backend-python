#!/usr/bin/env python3
"""
Computes the length of a list of sequences
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples with each string and its length.

    Args:
        lst (List[str]): The list of strings to measure.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple
        contains a string and its length.
    """
    return [(i, len(i)) for i in lst]
