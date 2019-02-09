"""
immutable lists
cannot be changed
"""

my_list = [1,2,3]
print(my_list)
print("-"*50)

my_list[0] = 0
print(my_list)
print("-"*50)

my_list.append(8)
print(my_list)
print("-"*50)

my_tuple = (1,2,3,2,4,5,6,3,1,2,2,1,1,1,1)
print(my_tuple)
print("-"*50)

#my_tuple[0] = 5
print("-"*50)

print(my_tuple[1])
print(my_tuple[1:-1])
print(my_tuple.index(2))
print("-"*50)

print(my_tuple.count(1))
print(my_tuple.count(2))
print(my_tuple.count(3))
print("-"*50)