cars = ['BMW',"Honda","VW",'Volvo']
print("-"*50)

print(len(cars))
print("-"*50)

cars.append("Kia")
print(cars)
print(len(cars))
print("-"*50)

cars.insert(1,"Jeep")
print(cars)
print("-"*50)

x = cars.index("Honda")
print(x)
print("-"*50)

y = cars.pop()
print(y)
print(cars)
print("-"*50)

cars.remove("Jeep")
print(cars)
print("-"*50)

print(cars)
slicing = cars[1:]
print(slicing)
print(cars)
print("-"*50)

print(cars)
slice2 = cars[-2:]
print(slice2)
print("-"*50)

cars.append("Audi")
print(cars)
cars.sort()
print(cars)
print("-"*50)

