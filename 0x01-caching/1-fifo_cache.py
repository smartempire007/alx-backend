#!/usr/bin/env python3
'''Create a class FIFOCache that inherits from BaseCaching and is a
caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for
    the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that
    BaseCaching.MAX_ITEMS:
    you must discard the first item put in cache (FIFO algorithm)
    you must print DISCARD: with the key discarded and following by
    a new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''a class FIFOCache that inherits from BaseCaching'''

    def __init__(self):
        '''init'''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''assign to the dictionary self.cache_data the item'''
        if key is None or item is None:
            return self.cache_data.update({key: item})

        # if key is not in cache_data
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.queue[0]
            self.cache_data.pop(discard)
            print('DISCARD: {}'.format(discard))
            self.queue.pop(0)
        return self.cache_data.update({key: item})

    def get(self, key):
        '''return the value in self.cache_data linked to key'''
        return self.cache_data.get(key, None)
