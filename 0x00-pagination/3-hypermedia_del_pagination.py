#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing the following key-value pairs:
        index: the current start index of the return page
        next_index: the next index to query with.
        page_size: the current page size
        data: the actual page of the dataset

        Args:
            index (int): The current start index of the return page
            page_size (int): The number of element per page
        Returns:
            Dict: A dictionary containing pagination information
        """
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        dataset_size = len(indexed_data)

        if index is None:
            index = 0

        if index >= dataset_size:
            return {
                    "index": index,
                    "next_index": None,
                    "page_size": page_size,
                    "data": []
                    }
        data = []
        current_index = index

        while len(data) < page_size and current_index < dataset_size:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index if current_index < dataset_size else None

        return {
                "index": index,
                "next_index": next_index,
                "page_size": page_size,
                "data": data
                }
