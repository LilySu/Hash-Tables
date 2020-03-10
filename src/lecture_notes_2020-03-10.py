class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key): # don't use htis outside of class
        return hash(key)

    def _hash_djb2(self, key):

        pass

    def _hash_mod(self,key): #future proffing so we might no want to use python's 
        #default hash, maybe we want to use different python runtimes
        #sha-256 hash we can abstract it away and change it later
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        #find index
        index = self._hash_mod(key)#turn key into index in our array
        if self.storage[index] is not None:
            print("ERROR: Key in use")
        else:
            self.storage[index] = value

    def remove(self, key):
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            self.storage[index] = None
        else:
            print("WARNInG: Key not found")

    def retrieve(self, key):
        index = self._hash_mod(key)
        return self.storage[index]

    def resize(self):
        '''Doubles capacity of hash table and 
        rehash all key value pairs'''
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for bucket_item in old_storage:
            self.insert(bucket_item.key, bucket_item.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
