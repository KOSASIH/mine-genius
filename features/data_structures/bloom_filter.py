class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = [False] * size

    def add(self, item):
        # adds an item to the bloom filter
        pass

    def __contains__(self, item):
        # checks if an item is in the bloom filter
        pass
