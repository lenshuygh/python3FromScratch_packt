"""
var scope
"""

a = 10

def test_method(a):
    """
    prints argument
    :param a: any
    :return: /
    """
    print("Value of local a = " + str(a))
    a = 2
    print("new local a value = " + str(a))

print("value of global a = " + str(a))
test_method(a)
print("value of global a = " + str(a))
print('-*'*50)

b = 10

def test_methodB():
    """
    prints argument
    :param b: any
    :return: /
    """
    global b
    print("Value of local a = " + str(b))
    b = 2
    print("new local a value = " + str(b))

print("value of global a = " + str(b))
test_methodB()
print("value of global a = " + str(b))
print('-*'*50)