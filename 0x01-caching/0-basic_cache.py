#!/usr/bin/env python3
"""Caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system without limit
    """
    def put(self, key: str, item: any) -> None:
        """
        Add an item to the cache

        Args:
            key (str): the key under which the item should be stored
            item (any): the item to be stored
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: str) -> any:
        """
        Get an item by key from the cache

        Args:
            key (str): The key of the item to retrieve

        Returns:
            any: the item stored in the cache or None if the key doesnt exist
        """
        return self.cache_data.get(key)
