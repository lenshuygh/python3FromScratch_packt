x= 0
while x < 10:
    print("the value of x is %d" %x)
    x += 1
    if x == 8:
        break
    print("this example is awesome")
    print('*'*20)

print('broke out of the loop')
print('--'*50)

x= 0
while x < 10:
    print("the value of x is %d" %x)
    x += 1
    if x == 5:
        continue
    print("this example is awesome")
    print('*'*20)


print('--'*50)

x = 0
while x < 10:
    print("x = " + str(x))
    x = x + 1
    if x == 8:
        break
    print("looping...")
else:
    print('else block !!!')

print('--'*50)