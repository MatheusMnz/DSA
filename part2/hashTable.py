# Building from scratch HashTable

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [None for i in range(self.MAX)]

    def get_hash(self, key):
        ascii_value = 0
        for char in key:
            ascii_value += ord(char)
        return ascii_value % self.MAX
    
    # Dunder method
    def __setitem__(self, key, val):
        hash_index = self.get_hash(key)
        self.array[hash_index] = val

    # Dunder method
    def __getitem__(self, key):
        hash_index = self.get_hash(key)
        return self.array[hash_index]
    
    def __delitem__(self, key):
        hash_index = self.get_hash(key)
        self.array[hash_index] = None

if __name__ == '__main__':
    t = HashTable()
    t['march 6'] = 130
    t['June 8'] = 2002
    print(t['march 6'])
    print(f'Hash Table After Deleting {t.array}')
    del t['June 8']
    print(f'Hash Table Before Deleting {t.array}')