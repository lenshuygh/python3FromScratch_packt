"""
oop
"""


class Car(object):
    def __init__(self, brand, model="550i"):
        self.brand = brand
        self.model = model

c1 = Car("VW")
print(c1.brand)
print(c1.model)
c1.brand = "Audi"
print(c1.brand)
print(c1.model)

c2 = Car("Benz","CLA")
print(c2.brand)
print(c2.model)
print(c1.brand)
