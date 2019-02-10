"""
built-in functions
"""
# max() largest number
l = [1,5,4,3,8,4,2,4,9,4,5,2]
print(max(l))
print(max(4,2,7,3,1))

def largest_num(*args):
    # print(max(args))
    return max(args)

print(largest_num(l))
print(largest_num(4,2,7,3,1))

print(min(4,2,7,3,1))
print(abs(-4))
print(abs(4))
print('-*'*50)

def print_type(a):
    print(type(a))

print_type(99)
print_type("Thor")
print_type(99.1)
print_type(l)