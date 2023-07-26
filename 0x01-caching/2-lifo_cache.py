#!/usr/bin/env python3
'''Create a class LIFOCache that inherits from BaseCaching and is
a caching system:

You must use self.cache_data - dictionary from the parent class
BaseCaching
You can overload def __init__(self): but don’t forget to call the
parent init: super().__init__()
def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value
    for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that
    BaseCaching.MAX_ITEMS:
    you must discard the last item put in cache (LIFO algorithm)
    you must print DISCARD: with the key discarded and following by a
    new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''a class LIFOCache that inherits from BaseCaching'''

    def __init__(self):
        '''init'''
        super().__init__()
        self.__queueing = []

    def put(self, key, item):
        '''assign to the dictionary self.cache_data the item value for
        the key key'''
        if not all([key, item]):
            return
        self.cache_data.update({key: item})

        if len(self.cache_data) <= self.MAX_ITEMS:
            if key not in self.__queueing:
                self.__queueing.append(key)
            else:
                self.__queueing.append(self.__queueing.pop(
                    self.__queueing.index(key)
                ))
            return

        if not key in self.__queueing:
            '''cache filled up'''
            popped_key = self.__queueing.pop()
            self.cache_data.pop(popped_key)
            print('DISCARD: {}'.format(popped_key))
            self.__queueing.append(key)

    def get(self, key):
        '''return the value in self.cache_data linked to key'''
        return self.cache_data.get(key, None)
