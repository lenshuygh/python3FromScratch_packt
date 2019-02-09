"""
usefull for generating numbers
creates sequence of numbers but doesn't save them in memory
"""

print(list(range(0,10)))

a= range(12,100,10)
print(a)
print(type(a))
print(list(a))
print('-*'*20)

a= range(0,20,6)
print(a)
print(type(a))
print(list(a))
print('-*'*20)

l = [1,2,3]
for num in l:
    print(num)
print('-*'*20)

for num in range(1,4):
    print(num)
print('-*'*20)
