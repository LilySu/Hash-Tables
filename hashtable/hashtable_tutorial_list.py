table = [[] for _ in range(10)]
def hashing_fun(x):
    return x%10


def insert(table,key,value):
    table[hashing_fun(key)].append(value)

print(hashing_fun(15))

print(table)
print(insert(table,15,'dog'))
print(table)

print(insert(table,117,'cat'))