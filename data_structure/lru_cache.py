"""

"""
from collections import OrderedDict


class LRUCache(object):

    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache.keys():
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return None

    def set(self, key, val):
        if len(self.cache) < self.max_size:
            self.cache[key] = val
        else:
            self.cache.popitem(last=False)
            self.cache[key] = val


if __name__ == "__main__":
    test_cache = LRUCache(5)
    test_cache.set(2, "hello")
    test_cache.set(3, "python")
    test_cache.set(4, "world")
    print(test_cache.cache)

    test_cache.get(3)
    print(test_cache.cache)

    test_cache.set(5, "my")
    test_cache.set(6, "name")
    test_cache.set(7, "is")
    print(test_cache.cache)
