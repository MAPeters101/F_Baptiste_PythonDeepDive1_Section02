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

min_length = 2
name = input("Please enter your name: ")
while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")

print("Hello, {0}".format(name))
print('-'*80)


