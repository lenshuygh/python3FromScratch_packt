my_string = 'abcabc'
for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')
print('--' * 50)

cars = ['bmw', 'benz', 'honda']
for car in cars:
    print(car)
print('--' * 50)

nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n * 10)
print('--' * 50)

d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k)
print('--' * 50)

d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
    print(k + " " + str(d[k]))
print('--' * 50)

for k,v in d.items():
    print(k + " -> " + str(v))
print('--' * 50)
