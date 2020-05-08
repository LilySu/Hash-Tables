# A hash function must be consistent (deterministic). Every time it receives the same input (like "aqua"), it must return the same output (like 4). If it’s not deterministic, it is not a hash function.
# Different input data should return different numbers. For example, if the input "aqua" returns 4, then the input "beige" should not return 4.
# A hash function must return numbers that are within a specific range.


class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 10
        self.storage = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        pass

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity
        h = 0
        for char in key:
            h += ord(char)
        return h % self.count

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.count >= self.capacity:
            print("Error full")
            return

        if key >= self.count:
            print("Index out of range")
            return

        for i in range(self.count, key, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[key] = value
        self.count += 1

        # if self.count
        # new_node = HashTableEntry(value)
        # cur = self.head
        # while cur.next != None & cur.value != new_node.value:
        #     cur = cur.next

        # cur.next = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # delete: 
        # find the hash index
        cur = self.djb2(key)
        # search the list for the key
        # if found, delete the node from the list (return the node or value)
        return cur.get_hash(key)
        # else return none


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        pass

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    print(ht.hash_index("line_1"))

    # ht.put("line_1", "Tiny hash table")
    # ht.put("line_2", "Filled beyond capacity")
    # ht.put("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # print("")
