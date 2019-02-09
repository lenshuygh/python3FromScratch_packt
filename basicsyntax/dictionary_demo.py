"""
data type to store key value pairs
items are in brackets { } -> key-value pairs , seperator is ,
{'k1':'v1",'k2':'v2'}
not sequenced, not indexed => it is mapped
"""

my_dict = {'cat1':"Thor","Cat2":'Smiegel'}
print(my_dict)
print("-"*50)

car = {'make': 'BMW', 'model': '550i', 'year':2016}
print(car)
print(car['model'])
print(car['year'])
print("-"*50)

print(len(car))
print("-"*50)

model = car['model']
print(model)
print("-"*50)

empty_dict = {}
print(empty_dict)
print("-"*50)

empty_dict['one'] = 1
print(empty_dict)
empty_dict["color"] = "black"
print(empty_dict)
print("-"*50)

sum = empty_dict['one']
sum *= 8
print(sum)
print("-"*50)

print(empty_dict)
empty_dict['one'] = empty_dict['one'] + 5
print(empty_dict)
print("-"*50)

