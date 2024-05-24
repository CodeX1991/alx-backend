#!/usr/bin/env python3
"""Caching system
"""

from collections import OrderedDict, defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Basic caching system without limit
    """
    def __init__(self):
        """
        Initialize the cache
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key: str, item: any) -> None:
        """
        Add an item to the cache

        Args:
            key (str): the key under which the item should be stored
            item (any): the item to be stored
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and usage info
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict()
            # Add new key-value pair and initialize frquency and usage order
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key: str) -> any:
        """
        Get an item by key from the cache

        Args:
            key (str): The key of the item to retrieve

        Returns:
            any: the item stored in the cache or None if the key doesnt exist
        """
        if key is None or key not in self.cache_data:
            return None
        # Update usage info
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

    def evict(self):
        """
        Find the least frequency used items
        """
        min_freq = min(self.frequency.values())
        min_freq_keys = [
                k for k, v in self.frequency.items() if v == min_freq]
        # Among those, find the least recentlyy used item
        for key in self.usage_order:
            if key in min_freq_keys:
                break
        # Remove the item from cache_data, frequency, and usage_order
        del self.cache_data[key]
        del self.frequency[key]
        del self.usage_order[key]
        print("DISCARD: " + key)

    def print_cache(self):
        """
        Print the contents of the cache in order
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(key + ": " + value)
