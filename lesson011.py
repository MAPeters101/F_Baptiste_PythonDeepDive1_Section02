i = 0
while i < 5:
    print(i)
    i += 1
print('-'*80)

i = 5
while True:
    print(i)
    if i >= 5:
        break
        print('something')
print('-'*80)

# min_length = 2
# name = input("Please enter your name: ")
# while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
#     name = input("Please enter your name: ")
#
# print("Hello, {0}".format(name))
# print('-'*80)

# min_length = 2
# while True:
#     name = input("Please enter your name: ")
#     if len(name) >= min_length and name.isprintable() and name.isalpha():
#         break
#
# print("Hello, {0}".format(name))
# print('.'*80)

a = 0
while a < 10:
    a += 1
    if a%2 == 0:
        continue
    print(a)
print('-'*80)

l = [1, 2, 3]
val = 10
found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
if not found:
    l.append(val)
print(l)
print('-'*80)





