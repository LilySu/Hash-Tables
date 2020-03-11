# '''
# Linked List hash table key/value pair
# '''
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
        self.curr_node = None
        
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        '''
        index = self._hash_mod(key)#turn key into index in our array
        if self.storage[index] is not None: # if there is something there
            while self.curr_node is not None:
                self.curr_node = self.curr_node.next
            self.curr_node = LinkedPair(key, value)
        else:
            self.storage[index] = value
            # if self.storage[index] != value:# update key and value if key matches
            #     self.storage[index] = value
            # if self.curr_node is None: # and if no node is there
            #     self.curr_node = LinkedPair(key, value) # insert as a node
            # while self.curr_node is not None: #until the node does not exist
            #     self.curr_node = self.curr_node.next # traverse through all nodes to the last one
            # self.curr_node = LinkedPair(key, value) # store key value in current node

        #     print("Error: Key in use")
        #     current = self.storage
        #     new_pair = LinkedPair(key, value)           
        #     exists = False
        #     while current:
        #         if current.key == key: #if no next break out of loop
        #             current.value = value
                    
        #             current = None
        #             exists = True
        #         current = current.next
        #     if not exists:
        #         currrent.next
        # else:
        #     self.storage[index] = value


        # index = self._hash_mod(key)#turn key into index in our array
        # if self.storage[index] is not None:
        #     print("ERROR: Key in use")
        # else:
        #     self.storage[index] = value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            self.storage[index] = None
        else:
            print("Warning: Key not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # for i in self.storage[index]:
        #     print(i)
        if self.curr_node != None:
            print(self.curr_node.value)
        return self.storage[index]
        # elif self.curr_node != None:
        #     if key == self.curr_node.key:
        #         return self.curr_node.value
        #     else:
        #         while self.curr_node.next != None: # (self.curr_node.value != self.storage[index]) and (self.curr_node.next != None):
        #             self.curr_node = self.curr_node.next

        #         if (self.curr_node.next == None) and (self.curr_node.key != key):
        #             return "Value does not exist"


    # def resize(self):
    #     '''
    #     Doubles the capacity of the hash table and
    #     rehash all key/value pairs.

    #     Fill this in.
    #     '''
    #     old_storage = self.storage
    #     self.capacity = self.capacity * 2
    #     self.storage = [None] * self.capacity

    #     # have some number of buckets and when there is too much items in the hash table, create a new hash table with a larger size and move all the items to the new hash table.
    #     for bucket_item in old_storage:
    #         self.insert(bucket_item.key, bucket_item.value)

    def resize(self):
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        for item in old_storage:
            self.insert(item.key, item.value)




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
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
