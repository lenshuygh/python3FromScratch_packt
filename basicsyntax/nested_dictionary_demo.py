"""
d= {'k1': {'nk1':'nv1','nk2','nv2'}}
"""

cars = {'bmw':{'model':'550i','year':2016},'benz':{'model':'E350','year':2015}}
print(cars)
print(cars['bmw'])
print(cars['benz']['model'])
cars['benz']['model'] = "E362"
print(cars['benz']['model'])
print(cars)

