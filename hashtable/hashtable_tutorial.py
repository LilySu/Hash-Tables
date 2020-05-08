class HashTable:
    def __init__(self):
        self.MAX = 10
        # we are storing key value pair
        self.arr = [[] for i in range(self.MAX)] #initiallizing 100 items in array

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # implement function to add something and get something
    def add(self,key,val): #def __setitem__
        h = self.get_hash(key)
        # self.arr[h] = val
        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0]==key: #if key exists
                self.arr[h][idx] = (key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val)) # if key does not exist in linked list

    def get(self,key): #def __getitem__
        h = self.get_hash(key)
        return self.arr[h]

    def delete(self,key): #def __delitem__
        h = self.get_hash(key)
        # self.arr[h] = None
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable()
t.add('march 6', 130)
t.add('march 6', 78)
t.add('march 8', 67)
t.add('march 9', 4)
t.add('march 17', 459)
t.delete('march 17')

print(t.arr)
# print(t.get('march 6'))
# print(t.get_hash('march 6'))