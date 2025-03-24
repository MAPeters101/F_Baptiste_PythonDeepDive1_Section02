
i = 0
while i < 5:
    print(i)
    i += 1
i = None
print('-'*80)

for i in range(5):
    print(i)
print('-'*80)

for i in [1,2,3,4]:
    print(i)
print()
for c in 'hello':
    print(c)
print()

for x in {'a', 'b', 'c', 4}:
    print(x)
print()
print('-'*80)

for x in [(1,2), (3,4), (5,6)]:
    print(x)
print()

for i,j in [(1,2), (3,4), (5,6)]:
    print(i,j)
print()
print('-'*80)

for i in range(5):
    if i == 3:
        continue
    print(i)
print()

for i in range(5):
    if i == 3:
        break
    print(i)
print()
print('-'*80)

for i in range(1, 8):
    print(i)
    if i%7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiples of 7 in the range')
print('-'*80)

for i in range(5):
    print('-'*20)
    try:
        10 / (i-3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always run')
    print(i)
print('-'*80)

s = 'hello'
for c in s:
    print(c)
print()

s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1
print()

s = 'hello'
for i in range(len(s)):
    print(i, s[i])
print()

s = 'hello'
for i, c in enumerate(s):
    print(i, c)
print()





print('-'*80)








