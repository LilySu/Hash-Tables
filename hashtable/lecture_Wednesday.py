# Load factor

# = # elements in list/ # of slots

# load factor is count of items, not items used. 

# put - you could insert or replace, so you can't count load factor

# 1. make a new bigger table/array
# 2. go through all the old elements and hash into the new list

# rule of thumb:
# if you resize bigger, double the size
# if you resize smaller, halve the size

# automatic resize - if load is greather than some factor, double hashtable
# if load < half the size of hashtable down to minimum
# imposed when you put, because that's when you potentially increase load factor