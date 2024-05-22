#!/usr/bin/env python3
"""Caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Basic caching system without limit
    """
    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.order = []

    def put(self, key: str, item: any) -> None:
        """
        Add an item to the cache

        Args:
            key (str): the key under which the item should be stored
            item (any): the item to be stored
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: " + oldest_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key: str) -> any:
        """
        Get an item by key from the cache

        Args:
            key (str): The key of the item to retrieve

        Returns:
            any: the item stored in the cache or None if the key doesnt exist
        """
        return self.cache_data.get(key)
