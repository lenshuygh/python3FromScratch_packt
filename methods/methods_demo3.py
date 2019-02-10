# positional parameters
# can be assigned a default value

def sum_nums(n1=2, n2=4):
    """
    Get the sum of 2 numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


print(sum_nums(10,20))
print(sum_nums())
print(sum_nums(8))
print(sum_nums(n2=8))
print(sum_nums(n2=1,n1=7))
print('-*' * 50)

def sum_numbers(n1, n2=4):
    """
    Get the sum of 2 numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


print(sum_numbers(10,20))
print(sum_numbers(8))
print(sum_numbers(2))
print(sum_numbers(1,n2=7))



print('-*' * 50)
