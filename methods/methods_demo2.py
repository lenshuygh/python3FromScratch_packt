def sum_nums(n1, n2):
    """
    Get the sum of 2 numbers
    :param n1:
    :param n2:
    :return:
    """
    print(n1 + n2)


sum_nums(10, 20)
print('-*' * 50)


def calc_sum(n1, n2):
    """
    returns the sum of 2 arguments
    :param n1: number
    :param n2: number
    :return: number
    """
    return n1 + n2


print(calc_sum(50, 5))
sum = calc_sum(5, 6)
print(sum)
print('-*' * 50)


def isMetro(city):
    l = ['sfo', 'nyc', 'la']
    if city.lower() in l:
        return True
    else:
        return False


print(isMetro("diepenbeek"))
print(isMetro("la"))
print(isMetro("La"))
print('-*' * 50)

string_add = sum_nums('one','two')
print(string_add)
print('-*' * 50)

string_add = sum_nums('one',2)
print(string_add)
print('-*' * 50)