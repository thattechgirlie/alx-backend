#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
