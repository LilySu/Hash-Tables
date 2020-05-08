class node:#sublcass of linked list
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head = node() # never contain data, not indexable, pointer placeholder

    def append(self,data): # ends new datapoint to end, also creates first element
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next # traverse through list if node is not none
        # when we are at the end of our list
        cur.next = new_node

    def length(self): #length useful to manage
        cur = self.head
        total = 0 
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

    # pull out data from a certain index
    def get(self,index):
        if index >= self.length():
            print("GET index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1
        
    def erase(self,index):
        if index >= self.length():
            print('ERASE index out of range')
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

my_list = linked_list()

# my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.erase(1)

# print("element at 2nd index: %d" % my_list.get(2))
my_list.display()