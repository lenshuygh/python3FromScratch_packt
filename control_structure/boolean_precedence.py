"""
1. not
2. and
3. or
"""

boolean_output = True or not False and False
print(boolean_output)
print('-'*10)

bool = 10 == 10 or 10 < 10 and 10 > 10
print(bool)
print('-'*10)

bool = (10 == 10 or 10 < 10) and 10 > 10
print(bool)
print('-'*10)

bool = 10 == 10 or (10 < 10 and 10 > 10)
print(bool)
print('-'*10)