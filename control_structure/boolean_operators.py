"""
and
or
not
"""

and_output = (10 == 10) and (10 > 9)
print(and_output)

and_output2 = (10 == 10) and (10 < 9)
print(and_output2)

and_ouput3 = (10 != 10) and (10 < 9)
print(and_ouput3)
print('-=-'*50)

or_1 = (10 == 10) or (10 > 9)
print(or_1)
or_2 = (10 == 10) or (10 < 9)
print(or_2)
or_3 = (10 != 10) or (10 < 9)
print(or_3)
print('-=-'*50)


not_1 = not(10 == 10)
print(not_1)
not_2 = not (10 != 10)
print(not_2)
print('-=-'*50)

