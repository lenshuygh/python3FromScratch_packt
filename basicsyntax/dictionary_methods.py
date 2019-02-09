car = {'make': 'BMW', 'model': '550i', 'year':2016}
cars = {'bmw':{'model':'550i','year':2016},'benz':{'model':'E350','year':2015}}

print(car)
print(car.keys())
print(car.values())
print('-'*50)

print(cars)
print(cars.keys())
print(cars.values())
print('-'*50)

print(car)
print(car.items())
print('-'*50)

print(cars)
print(cars.items())
print('-'*50)

car_copy = car.copy();
print(car)
print(car_copy)
print('-'*50)

print(car_copy)
car_copy.clear()
print(car_copy)
print('-'*50)

car_copy = car.copy()
print(car_copy)
car_copy.pop('model')
print(car_copy)
print('-'*50)

