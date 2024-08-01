#!/usr/bin/env python3
"""
Retrieves the first element of a sequence if it exists.
"""
from typing import List, Optional, Any


def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    Args:
        lst (List[Any]): The list from which to retrieve the first element.

    Returns:
        Optional[Any]: The first element of the list if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
