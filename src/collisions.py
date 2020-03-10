import random

def how_many_before_collision(buckets, loops=1):
    ''' Roll random hashes indexes into buckets and print
    how many rolls before a collision
    Run loops times'''
    for i in range(loops):
        tries = 0
        tried = set()

        # tried_list = []

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets # how long arrays we are using
            # if hash_index not in tried_list:
            if hash_index not in tried:
                #tried_list.append(hash_index)# different keys could hash to same thing, hence collision
                tried.add(hash_index)# different keys could hash to same thing, hence collision
                tries += 1

            else:
                # We have found a collision
                break

        print(f"{buckets} buckets, {tries} hashes before collision. ({tries/buckets * 100:.1f}%)")#formatting value to show 1 decimal

how_many_before_collision(10, 1)# 10 buckets 1 time

#collisions are inevitable
#linked list chaining 
#take our array, instead of putting a value, 
#we put linked list nodes in our hash table, 
#then when we get a collision, we just build out a chain