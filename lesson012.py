a = 10
b = 0
try:
    a/b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')
print('-'*80)

a = 0
b = 2
while a < 4:
    print('-'*20)
    a += 1
    b -= 1
    try:
        a/b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        continue
    finally:
        print('{0}, {1} - this always executes'.format(a, b))
    print('{0}, {1} - main loop'.format(a, b))
print('-'*80)

a = 0
b = 2
while a < 4:
    print('-'*20)
    a += 1
    b -= 1
    try:
        a/b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        break
    finally:
        print('{0}, {1} - this always executes'.format(a, b))
    print('{0}, {1} - main loop'.format(a, b))
print('-'*80)


a = 0
b = 10
while a < 4:
    print('-'*20)
    a += 1
    b -= 1
    try:
        a/b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        break
    finally:
        print('{0}, {1} - this always executes'.format(a, b))
    print('{0}, {1} - main loop'.format(a, b))
else:
    print('Code executed without a zero division error')
print('-'*80)


