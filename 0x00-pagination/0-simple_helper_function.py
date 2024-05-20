#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function should return a tuple

    Args:
        page (int): the page number
        page_size (int): number of element per page

    Return: a list for a particular pagination
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
