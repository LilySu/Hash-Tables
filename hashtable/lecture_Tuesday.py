# linear probing is a method of open addressing
# method to store things somewhere else
# collision and open resolution works hand-in-hand

# put: scan forward from hash index until we find either the key or Non
# If we find a deleted slot along the way, keep it in mind
# put the value there

# get: scan forward from the hash index until we find either the key or none
# return that

# delete: scan forward f
# Scan forward from the hash index until we find either the key, or None
# If we find the key, mark it as deleted

# collision resolution by chaining

# each slot of the hash table holds a linked list
# collisions are handled by adding multiple items to the same linked list

# slot

# index chain (linked list) - reference to head node
#------ -------------------
# 0 -> None
# 1 -> ('foo',12)
# 2 -> ('bar',30) -> ('baz',999)
# 3 -> None

# put('foo',12) # hashes to index 1
# put('bar',30) # hashes to index 2
# put('baz',999) # hashes to index 2 

# put:
# search the list for the key
# if it is there, replace the value
# if it's not, append a new record to the list

# doesn't matter if you use linked list nods or linked list class

# hash table is a linked list except increase size of hash table when it gets to big

#doubly linked list good for deleting but juggling pointers is hard.

# get: find the hash index
# search the list for the key
# if found, return the value
# else return none

# delete: 
# find the hash index
# search the list for the key
# if found, delte the node from the list (return the node or value)
# else return none

# as numbers grow, code grows from probing, exponentially for chaining